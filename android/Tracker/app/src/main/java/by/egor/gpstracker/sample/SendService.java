package by.egor.gpstracker.sample;

import android.app.Service;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.IBinder;
import android.util.Log;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONObject;

import by.egor.gpstracker.sample.activity.SampleActivity;

public class SendService extends Service {

    float latitude;
    float longitude;
    String url;

    @Override
    public void onCreate()
    {
        super.onCreate();
    }

    public int onStartCommand(Intent intent, int flags, int startId)
    {
        latitude = (float)intent.getExtras().getDouble(SampleActivity.LAT);
        longitude = (float)intent.getExtras().getDouble(SampleActivity.LON);
        url = intent.getExtras().getString(SampleActivity.URL);
        new HttpAsyncTask().execute(url);

        return super.onStartCommand(intent, flags, startId);
    }

    @Override
    public IBinder onBind(Intent intent)
    {
        // TODO: Return the communication channel to the service.
        throw new UnsupportedOperationException("Not yet implemented");
    }

    public static String POST(String url, float lat, float lon)
    {
        String json;

        try
        {
            HttpClient httpclient = new DefaultHttpClient();

            HttpPost httpPost = new HttpPost(url);

            JSONObject jsonObject = new JSONObject();
            jsonObject.accumulate("latitude", lat);
            jsonObject.accumulate("longitude", lon);

            json = jsonObject.toString();

            StringEntity se = new StringEntity(json);

            httpPost.setEntity(se);

            httpPost.setHeader("Accept", "application/json");
            httpPost.setHeader("Content-type", "application/json");

            HttpResponse httpResponse = httpclient.execute(httpPost);
        }
        catch (Exception e)
        {
            Log.d("InputStream", e.getLocalizedMessage());
        }

        return "";
    }

    private class HttpAsyncTask extends AsyncTask<String, Void, String>
    {
        @Override
        protected String doInBackground(String... urls)
        {
            return POST(urls[0], latitude, longitude);
        }

        @Override
        protected void onPostExecute(String result)
        {}
    }
}
