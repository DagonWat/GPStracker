package egor.by.beaconclient;

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
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;

public class MainActivity extends AppCompatActivity
{
    TextView txt;
    String fserver = "";
    String size = "";
    String serverIp = "ip";
    int socketId = 10000;

    public final static String BROADCAST_ACTION = "by.egor.serviceback";
    BroadcastReceiver br;

    public void decode(String a)
    {
        size = a;
        txt.setText(a);
    }

    public void decodeImage(byte[] a)
    {
        Bitmap bmp = BitmapFactory.decodeByteArray(a, 0, a.length);
        ImageView image = (ImageView) findViewById(R.id.pic);
        image.setImageBitmap(bmp);
    }

    public void startDiscovery(View view)
    {
        //Timer tim = new Timer();
        //TimerTask bthh = new MyTimerTask();
        //tim.schedule(bthh, 200, 500);

        Intent intent = new Intent(this, NewService.class);
        intent.putExtra("size", "18136");
        startService(intent);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txt = (TextView) findViewById(R.id.text);

        br = new BroadcastReceiver()
        {
            public void onReceive(Context context, Intent intent)
            {
                decodeImage(intent.getByteArrayExtra("result"));
            }
        };

        IntentFilter intFilt = new IntentFilter(BROADCAST_ACTION);
        registerReceiver(br, intFilt);

        //new Task().execute("");
    }

    public class Task extends AsyncTask<String, Void, String>
    {
        @Override
        protected String doInBackground(String... params)
        {
            fserver = "";
            try
            {
                Socket fromserver = new Socket(serverIp, socketId);
                PrintWriter out = new
                        PrintWriter(fromserver.getOutputStream(),true);
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
}



