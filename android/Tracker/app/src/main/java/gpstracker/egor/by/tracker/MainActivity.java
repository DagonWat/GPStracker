package gpstracker.egor.by.tracker;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;

import gpstracker.egor.by.tracker.activity.SampleActivity;

public class MainActivity extends AppCompatActivity
{
    Context context;
    float latitude;
    float longitude;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        latitude = 52.423542f;
        longitude = 21.345212f;

        context = getApplicationContext();

        startActivity(new Intent(this, SampleActivity.class));
    }

    public void sendCoords(View view)
    {
        Intent intent = new Intent(this, SendService.class);
        intent.putExtra("latitude", latitude);
        intent.putExtra("longitude", longitude);
        startService(intent);
    }
}
