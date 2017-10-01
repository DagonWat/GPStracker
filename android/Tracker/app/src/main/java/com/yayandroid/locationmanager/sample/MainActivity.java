package com.yayandroid.locationmanager.sample;

import android.app.ProgressDialog;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.location.Location;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.view.Window;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.yayandroid.locationmanager.constants.FailType;
import com.yayandroid.locationmanager.constants.ProcessType;
import com.yayandroid.locationmanager.sample.R;
import com.yayandroid.locationmanager.sample.SamplePresenter;
import com.yayandroid.locationmanager.sample.SamplePresenter.SampleView;
import com.yayandroid.locationmanager.sample.service.SampleService;

import java.util.Timer;
import java.util.TimerTask;

public class MainActivity extends AppCompatActivity implements SampleView {

    private IntentFilter intentFilter;
    private SamplePresenter samplePresenter;
    private ProgressDialog progressDialog;
    private TextView tvLatitude;
    private TextView tvLongitude;
    private EditText etUrl;
    private EditText etTime;
    private float latitude;
    private float longitude;
    public static final String URL = "url";
    public static final String LON = "longitude";
    public static final String LAT = "latitude";
    Intent intent;
    Timer tim1;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvLatitude = (TextView) findViewById(R.id.tvLatitude);
        tvLongitude = (TextView) findViewById(R.id.tvLongitude);
        etUrl = (EditText) findViewById(R.id.etUrl);
        etTime = (EditText) findViewById(R.id.etTime);
    }

    @Override
    protected void onResume() {
        super.onResume();
        registerReceiver(broadcastReceiver, getIntentFilter());
    }

    @Override
    protected void onPause() {
        super.onPause();
        unregisterReceiver(broadcastReceiver);
    }

    @Override
    public String getText() {
        return tvLatitude.getText().toString();
    }

    @Override
    public void setText(String text)
    {
        String[] s = text.split(",");

        String a = "Lat:  " + s[0].substring(6, 16);
        String b = "Lon:  " + s[1];

        tvLatitude.setText(a);
        tvLongitude.setText(b);

        latitude = Float.valueOf(s[0].substring(6, 16));
        longitude = Float.valueOf(s[1]);
    }

    public void stopSending(View view)
    {
        tim1.cancel();
    }

    private void sendCoords()
    {
        Intent sendIntent = new Intent(this, SendService.class);

        stopService(sendIntent);

        sendIntent.putExtra(LAT, latitude);
        sendIntent.putExtra(LON, longitude);
        sendIntent.putExtra(URL, etUrl.getText().toString());

        startService(sendIntent);

        //http://192.168.1.8:11000/api/sometest
    }

    public void startSending(View view)
    {
        tim1 = new Timer();
        TimerTask bthh = new LocationTimer();

        int period = Integer.parseInt(etTime.getText().toString());

        if (period >= 10)
        {
            tim1.schedule(bthh, 200, period * 1000);
        }
        else
        {
            Toast.makeText(getBaseContext(), "The minimum time is 10 s.", Toast.LENGTH_LONG).show();
            etTime.setText("10");
            tim1.schedule(bthh, 200, 10000);
        }

    }

    private void getLocation()
    {
        samplePresenter = new SamplePresenter(this);

        displayProgress();
        intent = new Intent(this, SampleService.class);
        startService(intent);
    }

    private class LocationTimer extends TimerTask {
        @Override
        public void run() {
            runOnUiThread( new Runnable(){
                @Override
                public void run() {
                    getLocation();
                    sendCoords();
                }
            });
        }
    }

    @Override
    public void updateProgress(String text) {
        if (progressDialog != null && progressDialog.isShowing()) {
            progressDialog.setMessage(text);
        }
    }

    @Override
    public void dismissProgress() {
        if (progressDialog != null && progressDialog.isShowing()) {
            progressDialog.dismiss();
        }
    }

    private void displayProgress() {
        if (progressDialog == null) {
            progressDialog = new ProgressDialog(this);
            progressDialog.getWindow().addFlags(Window.FEATURE_NO_TITLE);
            progressDialog.setMessage("Getting location...");
        }

        if (!progressDialog.isShowing()) {
            progressDialog.show();
        }
    }

    private IntentFilter getIntentFilter() {
        if (intentFilter == null) {
            intentFilter = new IntentFilter();
            intentFilter.addAction(SampleService.ACTION_LOCATION_CHANGED);
            intentFilter.addAction(SampleService.ACTION_LOCATION_FAILED);
            intentFilter.addAction(SampleService.ACTION_PROCESS_CHANGED);
        }
        return intentFilter;
    }

    private BroadcastReceiver broadcastReceiver = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            if (action.equals(SampleService.ACTION_LOCATION_CHANGED)) {
                samplePresenter.onLocationChanged((Location) intent.getParcelableExtra(SampleService.EXTRA_LOCATION));
            } else if (action.equals(SampleService.ACTION_LOCATION_FAILED)) {
                //noinspection WrongConstant
                samplePresenter.onLocationFailed(intent.getIntExtra(SampleService.EXTRA_FAIL_TYPE, FailType.UNKNOWN));
            } else if (action.equals(SampleService.ACTION_PROCESS_CHANGED)) {
                //noinspection WrongConstant
                samplePresenter.onProcessTypeChanged(intent.getIntExtra(SampleService.EXTRA_PROCESS_TYPE,
                        ProcessType.GETTING_LOCATION_FROM_CUSTOM_PROVIDER));
            }
        }
    };

    public void exit(View view)
    {
        finish();
        System.exit(0);
    }
}
