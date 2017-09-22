package gpstracker.egor.by.tracker;

import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONObject;

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
    }
    public void sendCoords(View view)
    {
        Intent intent = new Intent(this, SendService.class);
        intent.putExtra("latitude", latitude);
        intent.putExtra("longitude", longitude);
        startService(intent);
    }
}
