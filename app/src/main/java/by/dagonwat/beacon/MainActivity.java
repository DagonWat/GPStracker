package by.dagonwat.beacon;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothManager;
import android.bluetooth.le.BluetoothLeScanner;
import android.bluetooth.le.ScanCallback;
import android.bluetooth.le.ScanResult;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Timer;
import java.util.TimerTask;

public class MainActivity extends AppCompatActivity
{
    TextView txt;
    Map<String, String> beaconPicSize;
    BluetoothAdapter mBluetoothAdapter;
    BluetoothLeScanner mBluetoothScanner;
    BluetoothManager mBluetoothManager;
    boolean discoveryStarted = false;
    public ArrayList<Beacon> mBTDevices = new ArrayList<>();
    private LinearLayout llLog;
    Timer tim;

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
        llLog = (LinearLayout) findViewById(R.id.llLog);
        beaconPicSize = new HashMap<>();

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

        new GetInformation().execute("");
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
            tim.cancel();
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
                    mBluetoothScanner.startScan(leScanCallback);
                }
            });
        }
    }

    private ScanCallback leScanCallback = new ScanCallback()
    {
        @Override
        public void onScanResult(int callbackType, ScanResult result) {
            boolean alreadyFound = false;

            for (int i = 0; i < mBTDevices.size(); i++) {
                if (result.getDevice().getUuids().equals(mBTDevices.get(i).getId())) {
                    alreadyFound = true;
                }
            }

            if (!alreadyFound)
            {
                Beacon newBeacon = new Beacon(result.getDevice().getName(), result.getRssi());
                mBTDevices.add(newBeacon);

                TextView a = new TextView(context);
                String newLog = result.getDevice().getName();
                a.setText(newLog);
                llLog.addView(a);
            }
        }
    };
}



