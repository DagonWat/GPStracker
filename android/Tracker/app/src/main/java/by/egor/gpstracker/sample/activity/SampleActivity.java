package by.egor.gpstracker.sample.activity;

import android.app.ProgressDialog;
import android.content.Intent;
import android.location.Location;
import android.os.Bundle;
import android.support.v4.content.LocalBroadcastManager;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.yayandroid.locationmanager.base.LocationBaseActivity;
import com.yayandroid.locationmanager.configuration.Configurations;
import com.yayandroid.locationmanager.configuration.LocationConfiguration;
import com.yayandroid.locationmanager.constants.FailType;
import com.yayandroid.locationmanager.constants.ProcessType;

import by.egor.gpstracker.sample.MainActivity;
import by.egor.gpstracker.sample.R;
import by.egor.gpstracker.sample.SamplePresenter;
import by.egor.gpstracker.sample.SamplePresenter.SampleView;
import by.egor.gpstracker.sample.SendService;

public class SampleActivity extends LocationBaseActivity implements SampleView {

    private ProgressDialog progressDialog;
    private TextView locationText;

    public static final String URL = "url";
    public static final String LON = "longitude";
    public static final String LAT = "latitude";

    private EditText etUrl;

    private SamplePresenter samplePresenter;

    Button btnSend;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.sample_activity);

        locationText = (TextView) findViewById(R.id.tvCoords);
        btnSend = (Button) findViewById(R.id.btSend);
        etUrl = (EditText) findViewById(R.id.etUrl);

        samplePresenter = new SamplePresenter(this);
        getLocation();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        samplePresenter.destroy();
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

    public void sendBack(View view)
    {
        double[] coords = samplePresenter.getCoords();

        Intent sendIntent = new Intent(this, SendService.class);

        sendIntent.putExtra(LAT, Float.parseFloat(locationText.getText().toString().substring(0, 10)));

        sendIntent.putExtra(LON, Float.parseFloat(locationText.getText().toString().substring(11, 22)));
        sendIntent.putExtra(URL, etUrl.getText().toString());

        startService(sendIntent);
    }
}