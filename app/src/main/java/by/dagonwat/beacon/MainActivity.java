package by.dagonwat.beacon;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothManager;
import android.bluetooth.le.BluetoothLeScanner;
import android.bluetooth.le.ScanCallback;
import android.bluetooth.le.ScanResult;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.drawable.ClipDrawable;
import android.graphics.drawable.ColorDrawable;
import android.graphics.drawable.Drawable;
import android.graphics.drawable.GradientDrawable;
import android.graphics.drawable.LayerDrawable;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ProgressBar;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.TimeZone;
import java.util.Timer;
import java.util.TimerTask;

public class MainActivity extends AppCompatActivity
{
    TextView txt;
    TextView txtSize;
    Map<String, String> beaconPicSize;
    BluetoothAdapter mBluetoothAdapter;
    BluetoothLeScanner mBluetoothScanner;
    BluetoothManager mBluetoothManager;
    boolean discoveryStarted = false;
    public ArrayList<Beacon> mBTDevices;
    private LinearLayout llVer;
    private LinearLayout llHor;
    GradientDrawable progressGradientDrawable = new GradientDrawable(
            GradientDrawable.Orientation.LEFT_RIGHT, new int[]{
            0xff1e90ff,0xff006ab6,0xff367ba8});
    ClipDrawable progressClipDrawable = new ClipDrawable(
            progressGradientDrawable, Gravity.LEFT, ClipDrawable.HORIZONTAL);
    Drawable[] progressDrawables = {
            new ColorDrawable(0xffffffff),
            progressClipDrawable, progressClipDrawable};
    LayerDrawable progressLayerDrawable = new LayerDrawable(progressDrawables);
    ProgressBar pb;
    Timer tim;
    private SharedPreferences sharedPref;

    //ip address and socket from which we will get info
    public static final String SERVER_NUM = "111.222.111.101";
    public static final int SOCKET_NUM = 10000;

    public final static String BROADCAST_ACTION = "by.dagonwat.serviceback";
    public final static String SIZE = "size";
    public final static String SERVER = "server";
    public final static String SOCKET = "socket";

    BroadcastReceiver br;
    Context context;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        context = this;

        txt = (TextView) findViewById(R.id.text);
        llVer = (LinearLayout) findViewById(R.id.llVertical);
        llHor = new LinearLayout(this);
        beaconPicSize = new HashMap<>();
        mBTDevices = new ArrayList<>();

        sharedPref = this.getPreferences(Context.MODE_PRIVATE);
        int listSize = sharedPref.getInt("size", 0);

        txtSize = (TextView) findViewById(R.id.size);
        txtSize.setText(String.valueOf(listSize));

        TextView a = new TextView(context);
        a.setText("first");
        llHor.addView(a);

        pb = new ProgressBar(this);
        pb.setProgress(89);

        progressLayerDrawable.setId(0, android.R.id.background);
        progressLayerDrawable.setId(1, android.R.id.secondaryProgress);
        progressLayerDrawable.setId(2, android.R.id.progress);

        pb.setProgressDrawable(progressLayerDrawable);

        llHor.addView(pb);

        llVer.addView(llHor);

        for (int i = 0; i < listSize; i++)
        {
            /*String beaconName = sharedPref.getString(String.valueOf(i), "");
            int beaconInt = sharedPref.getInt(beaconName, 0);
            long beaconLastSeen = sharedPref.getLong(beaconName + "time", 0);
            Beacon newBeacon = new Beacon(beaconName, beaconInt, beaconLastSeen);
            mBTDevices.add(newBeacon);

            TextView a = new TextView(context);
            String newLog = beaconName;
            a.setText(newLog);
            //llLog.addView(a);*/
        }

        br = new BroadcastReceiver()
        {
            public void onReceive(Context context, Intent intent)
            {
                decodeImage(intent.getByteArrayExtra("result"));
            }
        };

        IntentFilter intFilt = new IntentFilter(BROADCAST_ACTION);
        registerReceiver(br, intFilt);

        mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        mBluetoothManager = (BluetoothManager) getSystemService(Context.BLUETOOTH_SERVICE);
        mBluetoothScanner = mBluetoothAdapter.getBluetoothLeScanner();

        //new GetInformation().execute("");
    }

    @Override
    protected void onDestroy()
    {
        super.onDestroy();

        SharedPreferences.Editor editor = sharedPref.edit();
        editor.putInt("size", mBTDevices.size());

        for (int i = 0; i < mBTDevices.size(); i++)
        {
            editor.putString(String.valueOf(i), mBTDevices.get(i).getName());
            editor.putInt(mBTDevices.get(i).getName(), mBTDevices.get(i).getTxPower());
            editor.putLong(mBTDevices.get(i).getName() + "time", mBTDevices.get(i).getLastSeen());
        }

        editor.apply();
    }

    //decode the only string server gives us into arrays
    private void decode(String a)
    {
        String[] parts = a.split("-");

        for (int i = 0; i < parts.length; i += 2)
        {
            //id : picSize
            beaconPicSize.put(parts[i], parts[i + 1]);
        }
    }

    //blit the image of beacon
    public void decodeImage(byte[] a)
    {
        Bitmap bmp = BitmapFactory.decodeByteArray(a, 0, a.length);
        ImageView image = (ImageView) findViewById(R.id.pic);
        image.setImageBitmap(bmp);
    }

    //start looking for beacons near
    public void startDiscovery(View view)
    {
        if (!discoveryStarted)
        {
            discoveryStarted = true;
            tim = new Timer();
            TimerTask bthh = new MyTimerTask();
            tim.schedule(bthh, 200, 500);
        }
    }

    public void stopDiscovery(View view)
    {
        if (discoveryStarted)
        {
            discoveryStarted = false;
        }
    }

    public void askPicture(String id)
    {
        Intent intent = new Intent(this, GetImageService.class);
        intent.putExtra(SIZE, beaconPicSize.get(id));
        intent.putExtra(SERVER, SERVER_NUM);
        intent.putExtra(SOCKET, SOCKET_NUM);
        startService(intent);
    }

    public class GetInformation extends AsyncTask<String, Void, String>
    {
        @Override
        protected String doInBackground(String... params)
        {
            String fserver = "";
            try
            {
                Socket fromserver = new Socket(SERVER_NUM, SOCKET_NUM);
                BufferedReader in  = new BufferedReader(new
                        InputStreamReader(fromserver.getInputStream()));
                fserver = in.readLine();
            }
            catch (IOException e)
            {
                Thread.interrupted();
            }

            return fserver;
        }

        @Override
        protected void onPostExecute(String result)
        {
            decode(result);
        }

        @Override
        protected void onPreExecute() {}

        @Override
        protected void onProgressUpdate(Void... values) {}
    }

    class MyTimerTask extends TimerTask
    {
        @Override
        public void run()
        {
            AsyncTask.execute(new Runnable()
            {
                @Override
                public void run()
                {
                    if (discoveryStarted)
                    {
                        mBluetoothScanner.startScan(leScanCallback);
                    }
                    killOldBeacons();
                }
            });
        }
    }

    private ScanCallback leScanCallback = new ScanCallback()
    {
        @Override
        public void onScanResult(int callbackType, ScanResult result)
        {
            BluetoothDevice device = result.getDevice();
            if (device.getName() != null)
            {
                boolean alreadyFound = false;

                for (int i = 0; i < mBTDevices.size(); i++) {
                    if (result.getDevice().getName().equals(mBTDevices.get(i).getName())) {
                        alreadyFound = true;
                    }
                }

                if (!alreadyFound)
                {
                    Beacon newBeacon = new Beacon(result.getDevice().getName(), result.getRssi(), getSeconds());
                    mBTDevices.add(newBeacon);

                    TextView a = new TextView(context);
                    String newLog = result.getDevice().getName();
                    a.setText(newLog);
                    //llLog.addView(a);
                }

                txt.setText("");
            }
        }
    };

    public void killOldBeacons()
    {
        for (int i = 0; i < mBTDevices.size(); i++)
        {
            if (getSeconds() - mBTDevices.get(i).getLastSeen() > 30)
            {
                mBTDevices.remove(i);
                txtSize.setText(String.valueOf(mBTDevices.size()));
                i--;
            }
        }
    }

    public long getSeconds()
    {
        return System.currentTimeMillis();
    }
}



