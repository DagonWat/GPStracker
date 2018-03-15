package by.egor.gpstracker.sample;
import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.PowerManager;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.location.Location;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.yayandroid.locationmanager.LocationManager;
import com.yayandroid.locationmanager.configuration.DefaultProviderConfiguration;
import com.yayandroid.locationmanager.configuration.LocationConfiguration;
import com.yayandroid.locationmanager.configuration.PermissionConfiguration;
import com.yayandroid.locationmanager.constants.FailType;
import com.yayandroid.locationmanager.constants.ProcessType;
import com.yayandroid.locationmanager.constants.ProviderType;
import com.yayandroid.locationmanager.listener.LocationListener;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.TimeZone;
import java.util.Timer;
import java.util.TimerTask;

public class MainActivity extends AppCompatActivity implements LocationListener {
    private LocationManager locationManager;

    private TextView textLat;
    private TextView textLon;
    private EditText etTime;
    private EditText etToken;
    private LinearLayout llLog;
    Button btnSend;
    ArrayList<TextView> tvLog = new ArrayList<>();
    private Context context;

    public static final String URL = "url";
    public static final String TOK = "token";
    public static final String LON = "longitude";
    public static final String LAT = "latitude";

    PowerManager pm;
    PowerManager.WakeLock wl;

    double lat, lon;
    String tok;
    boolean isSending;
    boolean offClicked;
    Timer tim1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        context = this;

        isSending = false;
        offClicked = false;

        textLat = findViewById(R.id.tvLat);
        textLon = findViewById(R.id.tvLon);

        btnSend = findViewById(R.id.btSend);
        etTime = findViewById(R.id.etTime);
        etToken = findViewById(R.id.etToken);
        llLog = findViewById(R.id.llLog);

        pm = (PowerManager) getSystemService(Context.POWER_SERVICE);
        wl = pm.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, "Tag");

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


        locationManager = new LocationManager.Builder(getApplicationContext())
                .configuration(getLocationConfiguration())
                .activity(this)
                .notify(this)
                .build();
        LocationManager.enableLog(true);
    }

    @Override
    protected void onDestroy()
    {
        locationManager.onDestroy();
        super.onDestroy();
    }

    public void start(View view)
    {
        btnSend.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                continue_sending();
            }
        });
        wl.acquire();
        locationManager.get();
    }

    public void continue_sending()
    {
        offClicked = false;
    }

    public void startSending()
    {
        if (!isSending && !offClicked)
        {
            wl.acquire();
            tim1 = new Timer();
            TimerTask bthh = new LocationTimer();

            int period = Integer.parseInt(etTime.getText().toString());
            tok = etToken.getText().toString();

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
    }

    public void stopSending(View view)
    {
        if (isSending) {
            tim1.cancel();

            TextView a = new TextView(this);
            String newLog = "[" + getTime() + "]: Stop sending.";
            a.setText(newLog);
            tvLog.add(a);

            llLog.addView(tvLog.get(tvLog.size() - 1));

            isSending = false;
            offClicked = true;

            wl.release();
        }
    }


    public LocationConfiguration getLocationConfiguration() {
        return new LocationConfiguration.Builder()
                .keepTracking(true)
                .askForPermission(new PermissionConfiguration.Builder()
                        .build())
                .useDefaultProviders(new DefaultProviderConfiguration.Builder()
                        .requiredTimeInterval(1 * 1000) //1 second
                        .requiredDistanceInterval(0)
                        .acceptableAccuracy(4.0f)
                        .acceptableTimePeriod(4 * 1000) //4 seconds
                        .gpsMessage("Turn on GPS?")
                        .setWaitPeriod(ProviderType.GPS, 200 * 1000) //200 seconds
                        .setWaitPeriod(ProviderType.NETWORK, 20 * 1000) //20 seconds
                        .build())
                .build();
    }

    @Override
    public void onLocationFailed(@FailType int failType) {
        locationManager.get();
    }

    @Override
    public void onLocationChanged(Location location) {
        textLat.setText("Lat:  " + String.valueOf(location.getLatitude()).substring(0, 7));
        textLon.setText("Lon:  " + String.valueOf(location.getLongitude()).substring(0, 7));

        startSending();
        isSending = true;

        lat = location.getLatitude();
        lon = location.getLongitude();
    }

    private class LocationTimer extends TimerTask {
        @Override
        public void run() {
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    sendCoords();

                    TextView a = new TextView(context);
                    String newLog = "[" + getTime() + "]: Send coordinates: " + lat + "," + lon;
                    a.setText(newLog);
                    tvLog.add(a);

                    llLog.addView(tvLog.get(tvLog.size() - 1));
                }
            });
        }
    }

    public void sendCoords()
    {
        Intent sendIntent = new Intent(this, SendService.class);

        sendIntent.putExtra(LAT, lat);
        sendIntent.putExtra(LON, lon);
        sendIntent.putExtra(TOK, tok);
        sendIntent.putExtra(URL, "http://tracker-dev.sharkus.net/api/tracker");

        startService(sendIntent);
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
    public void onProcessTypeChanged(@ProcessType int processType) {
    }

    @Override
    public void onPermissionGranted(boolean alreadyHadPermission) {
    }

    @Override
    public void onStatusChanged(String provider, int status, Bundle extras) {
    }

    @Override
    public void onProviderEnabled(String provider) {
    }

    @Override
    public void onProviderDisabled(String provider) {
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
        this.finishAffinity();
    }
}
