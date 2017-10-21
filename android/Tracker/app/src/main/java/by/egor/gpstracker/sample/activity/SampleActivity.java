package by.egor.gpstracker.sample.activity;

import android.Manifest;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Location;
import android.os.Bundle;
import android.os.PowerManager;
import android.support.annotation.NonNull;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.yayandroid.locationmanager.base.LocationBaseActivity;
import com.yayandroid.locationmanager.configuration.Configurations;
import com.yayandroid.locationmanager.configuration.LocationConfiguration;
import com.yayandroid.locationmanager.constants.FailType;
import com.yayandroid.locationmanager.constants.ProcessType;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.TimeZone;
import java.util.Timer;
import java.util.TimerTask;

import by.egor.gpstracker.sample.R;
import by.egor.gpstracker.sample.SamplePresenter;
import by.egor.gpstracker.sample.SamplePresenter.SampleView;
import by.egor.gpstracker.sample.SendService;

public class SampleActivity extends LocationBaseActivity implements SampleView
{

    private ProgressDialog progressDialog;
    private TextView locationText;
    private EditText etUrl;
    private EditText etTime;
    private LinearLayout llLog;
    private double[] coords;
    Button btnSend;
    ArrayList<TextView> tvLog = new ArrayList<>();

    PowerManager pm;
    PowerManager.WakeLock wl;
    int FLAG_KEEP_SCREEN_ON = 128;

    public static final String URL = "url";
    public static final String LON = "longitude";
    public static final String LAT = "latitude";

    private Context context;

    private SamplePresenter samplePresenter;

    Timer tim1;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.sample_activity);
        context = this;

        locationText = (TextView) findViewById(R.id.tvCoords);
        btnSend = (Button) findViewById(R.id.btSend);
        etUrl = (EditText) findViewById(R.id.etUrl);
        etTime = (EditText) findViewById(R.id.etTime);
        llLog = (LinearLayout) findViewById(R.id.llLog);

        pm = (PowerManager)context.getSystemService(Context.POWER_SERVICE);
        wl = pm.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, "MyWakelockTag");
        wl.acquire();

        TextView a = new TextView(this);
        String newLog = "[" + getTime() + "]: Application started!";
        a.setText(newLog);
        tvLog.add(a);

        llLog.addView(tvLog.get(tvLog.size() - 1));

        askForPermission(Manifest.permission.ACCESS_FINE_LOCATION, 1);
        askForPermission(Manifest.permission.ACCESS_COARSE_LOCATION, 1);
        askForPermission(Manifest.permission.WRITE_EXTERNAL_STORAGE, 1);
        askForPermission(Manifest.permission.INTERNET, 1);
        askForPermission(Manifest.permission.ACCESS_WIFI_STATE, 1);

        samplePresenter = new SamplePresenter(this);
        getLocation();
    }

    @Override
    protected void onDestroy()
    {
        super.onDestroy();
        wl.release();
        samplePresenter.destroy();
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);


        switch (requestCode) {
            case 1:
                if (grantResults.length > 0
                        && grantResults[0] == PackageManager.PERMISSION_GRANTED) {

                    Toast.makeText(this, "Permission granted", Toast.LENGTH_SHORT).show();
                }
                break;
        }
    }

    private void askForPermission(String permission, Integer requestCode) {
        if (ContextCompat.checkSelfPermission(this, permission) != PackageManager.PERMISSION_GRANTED) {

            if (ActivityCompat.shouldShowRequestPermissionRationale(this, permission)) {

                ActivityCompat.requestPermissions(this, new String[]{permission}, requestCode);

            } else {

                ActivityCompat.requestPermissions(this, new String[]{permission}, requestCode);
            }
        } else {
            Toast.makeText(this, "" + permission + " is already granted.", Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    public LocationConfiguration getLocationConfiguration() {
        return Configurations.defaultConfiguration("Gimme the permission!", "Would you mind to turn GPS on?");
    }

    @Override
    public void onLocationChanged(Location location) {
        samplePresenter.onLocationChanged(location);
    }

    @Override
    public void onLocationFailed(@FailType int failType) {
        samplePresenter.onLocationFailed(failType);
    }

    @Override
    public void onProcessTypeChanged(@ProcessType int processType) {
        samplePresenter.onProcessTypeChanged(processType);
    }

    @Override
    protected void onResume() {
        super.onResume();

        if (getLocationManager().isWaitingForLocation()
                && !getLocationManager().isAnyDialogShowing()) {
            displayProgress();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();

        dismissProgress();
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

    @Override
    public String getText() {
        return locationText.getText().toString();
    }

    @Override
    public void setText(String text) {
        locationText.setText(text);
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

    private class LocationTimer extends TimerTask {
        @Override
        public void run() {
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    sendCoords();

                    TextView a = new TextView(context);
                    String newLog = "[" + getTime() + "]: Send coordinates: " + coords[0] + "," + coords[1];
                    a.setText(newLog);
                    tvLog.add(a);

                    llLog.addView(tvLog.get(tvLog.size() - 1));
                }
            });
        }
    }

    public void startSending(View view)
    {
        tim1 = new Timer();
        TimerTask bthh = new LocationTimer();

        int period = Integer.parseInt(etTime.getText().toString());

        if (period >= 20)
        {
            tim1.schedule(bthh, 200, period * 1000);
        }
        else
        {
            Toast.makeText(getBaseContext(), "The minimum time is 20 s.", Toast.LENGTH_LONG).show();
            period = 20;
            etTime.setText("20");
            tim1.schedule(bthh, 200, 20000);
        }

        TextView a = new TextView(this);
        String newLog = "[" + getTime() + "]: Start sending location with " + period + "s period.";
        a.setText(newLog);
        tvLog.add(a);

        llLog.addView(tvLog.get(tvLog.size() - 1));
    }

    public void stopSending(View view)
    {
        tim1.cancel();

        TextView a = new TextView(this);
        String newLog = "[" + getTime() + "]: Stop sending.";
        a.setText(newLog);
        tvLog.add(a);

        llLog.addView(tvLog.get(tvLog.size() - 1));
    }

    public void sendCoords()
    {
        Intent sendIntent = new Intent(this, SendService.class);

        coords = samplePresenter.getCoords();

        sendIntent.putExtra(LAT, coords[0]);
        sendIntent.putExtra(LON, coords[1]);
        sendIntent.putExtra(URL, etUrl.getText().toString());

        startService(sendIntent);
    }

    public String getTime()
    {
        Calendar cal = Calendar.getInstance(TimeZone.getTimeZone("GMT+1:00"));
        Date currentLocalTime = cal.getTime();
        DateFormat date = new SimpleDateFormat("HH:mm:ss");
        date.setTimeZone(TimeZone.getTimeZone("GMT+3:00"));
        String localTime = date.format(currentLocalTime);

        return localTime;
    }

    public void exit(View view)
    {
        finish();
        System.exit(0);
    }
}