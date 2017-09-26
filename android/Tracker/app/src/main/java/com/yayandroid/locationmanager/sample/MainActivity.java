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
import android.view.Window;
import android.widget.TextView;

import com.yayandroid.locationmanager.constants.FailType;
import com.yayandroid.locationmanager.constants.ProcessType;
import com.yayandroid.locationmanager.sample.R;
import com.yayandroid.locationmanager.sample.SamplePresenter;
import com.yayandroid.locationmanager.sample.SamplePresenter.SampleView;
import com.yayandroid.locationmanager.sample.service.SampleService;

public class MainActivity extends AppCompatActivity implements SampleView {

    private IntentFilter intentFilter;
    private SamplePresenter samplePresenter;
    private ProgressDialog progressDialog;
    private TextView tvLatitude;
    private TextView tvLongitude;
    private float latitude;
    private float longitude;
    Intent intent;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvLatitude = (TextView) findViewById(R.id.latitude);
        tvLongitude = (TextView) findViewById(R.id.longitude);
        samplePresenter = new SamplePresenter(this);

        displayProgress();
        intent = new Intent(this, SampleService.class);
        startService(intent);
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

        tvLatitude.setText(s[0].substring(0, 10));
        tvLongitude.setText(s[1]);

        latitude = Float.valueOf(s[0].substring(0, 10));
        longitude = Float.valueOf(s[1]);

        Intent intent = new Intent(this, SendService.class);
        intent.putExtra("latitude", latitude);
        intent.putExtra("longitude", longitude);
        startService(intent);
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
}
