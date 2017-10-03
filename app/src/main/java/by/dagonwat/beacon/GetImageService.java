package by.dagonwat.beacon;


import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.os.Binder;
import android.os.Bundle;
import android.os.IBinder;
import android.util.Log;
import android.widget.ImageView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;

/**
 * Created by egor on 23.8.17.
 */

public class GetImageService extends Service
{
    String size = "";

    @Override
    public void onCreate()
    {
        super.onCreate();
    }

    public int onStartCommand(Intent intent, int flags, int startId)
    {
        size = intent.getExtras().getString(MainActivity.SIZE);
        new GetImage().execute(size);

        return super.onStartCommand(intent, flags, startId);
    }

    @Override
    public IBinder onBind(Intent intent)
    {
        return null;
    }

    @Override
    public void onDestroy() { }

    public void sendBack(byte[] result)
    {
        Intent intent = new Intent(MainActivity.BROADCAST_ACTION);
        intent.putExtra("result", result);
        sendBroadcast(intent);

        stopSelf();
    }

    class GetImage extends AsyncTask<String, Void, byte[]>
    {
        @Override
        protected byte[] doInBackground(String... params)
        {
            String serverIp = "ip";
            int socketId = 10000;
            String sizeP = params[0];
            byte[] fserver = {(byte) 0x0};


            try
            {
                Log.d("Service", "start reading");

                Socket fromserver = new Socket(serverIp, socketId);
                PrintWriter out = new
                        PrintWriter(fromserver.getOutputStream(), true);

                BufferedReader in  = new BufferedReader(new
                        InputStreamReader(fromserver.getInputStream()));

                int s = Integer.parseInt(sizeP);

                DataInputStream dIn = new DataInputStream(fromserver.getInputStream());
                fserver = new byte[s];
                dIn.readFully(fserver, 0, fserver.length);

                fromserver.close();
            }
            catch (IOException e)
            {
                Thread.interrupted();
            }

            return fserver;
        }

        @Override
        protected void onPostExecute(byte[] result)
        {
            sendBack(result);
        }

        @Override
        protected void onPreExecute() {}

        @Override
        protected void onProgressUpdate(Void... values) {}
    }

}