package gpstracker.egor.by.tracker;

import android.app.AlertDialog;
import android.content.Context;
import android.os.AsyncTask;
import android.os.Looper;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.params.HttpConnectionParams;
import org.apache.http.params.HttpParams;
import org.json.JSONException;
import org.json.JSONObject;
import com.loopj.android.http.*;

import java.io.InputStream;

public class MainActivity extends AppCompatActivity
{
    Context context;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        new HttpAsyncTask().execute("");

        context = getApplicationContext();
    }

    public void sendCoords(View view)
    {
    }

    public static String POST(String url)
    {
        InputStream inputStream = null;
        String result = "";
        try
        {

            // 1. create HttpClient
            HttpClient httpclient = new DefaultHttpClient();

            // 2. make POST request to the given URL
            HttpPost httpPost = new HttpPost(url);

            String json = "";

            // 3. build jsonObject
            JSONObject jsonObject = new JSONObject();
            jsonObject.accumulate("latitude", 41);

            // 4. convert JSONObject to JSON to String
            json = jsonObject.toString();

            // ** Alternative way to convert Person object to JSON string usin Jackson Lib
            // ObjectMapper mapper = new ObjectMapper();
            // json = mapper.writeValueAsString(person);

            // 5. set json to StringEntity
            StringEntity se = new StringEntity(json);

            // 6. set httpPost Entity
            httpPost.setEntity(se);

            // 7. Set some headers to inform server about the type of the content
            httpPost.setHeader("Accept", "application/json");
            httpPost.setHeader("Content-type", "application/json");

            // 8. Execute POST request to the given URL
            HttpResponse httpResponse = httpclient.execute(httpPost);

            result = "DID WORK";

        }
        catch (Exception e)
        {
            Log.d("InputStream", e.getLocalizedMessage());
        }

        // 11. return result
        return result;
    }

    private class HttpAsyncTask extends AsyncTask<String, Void, String>
    {
        @Override
        protected String doInBackground(String... urls)
        {
            return POST("http://192.168.1.8:11000/api/sometest.json");
        }
        // onPostExecute displays the results of the AsyncTask.
        @Override
        protected void onPostExecute(String result)
        {
            Toast.makeText(getBaseContext(), "Data Sent!", Toast.LENGTH_LONG).show();
        }
    }
}

/*
try
            {
                URL url = new URL("http://192.168.1.8:11000/api/sometest.json");
                HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
                urlConnection.setDoOutput(true);
                urlConnection.setRequestMethod("POST");
                urlConnection.setRequestProperty("Content-Type", "application/json");
                urlConnection.setChunkedStreamingMode(0);
                urlConnection.connect();

                OutputStreamWriter out = new OutputStreamWriter(urlConnection.getOutputStream());

                JSONObject jsonObject = new JSONObject();
                jsonObject.accumulate("latitude", 99);

                DataOutputStream printout = new DataOutputStream(urlConnection.getOutputStream ());
                printout.writeBytes(URLEncoder.encode(jsonObject.toString(), "UTF-8"));
                printout.flush ();
                printout.close ();

                Toast toast = Toast.makeText(context, "Send successfully.", Toast.LENGTH_SHORT);
                toast.show();

                urlConnection.disconnect();
            }
            catch (MalformedURLException e)
            {
                Toast toast = Toast.makeText(context, "Can't connect to the server.", Toast.LENGTH_SHORT);
                toast.show();
            }
            catch (IOException e)
            {
                Toast toast = Toast.makeText(context, "Can't post to server.", Toast.LENGTH_SHORT);
                toast.show();
            }
            catch (JSONException e)
            {
                Toast toast = Toast.makeText(context, "Can't create JSON", Toast.LENGTH_SHORT);
                toast.show();
            }





try
            {
                AsyncHttpClient client = new AsyncHttpClient();
                JSONObject obj = new JSONObject();

                obj.put("latitude", 99);
                StringEntity entity = new StringEntity(obj.toString());

                client.post(getApplicationContext(), "Your_URL", entity, "application/json", new TextHttpResponseHandler() {
                    @Override
                    public void onFailure(int statusCode, Header[] headers, String responseString, Throwable throwable) {
                        Log.d("LoginActivity","Failed");
                        Log.d("LoginActivity","body " + responseString);
                    }

                    @Override
                    public void onSuccess(int statusCode, Header[] headers, String responseString) {
                        Log.d("LoginActivity","data " + responseString);
                        try {
                            JSONObject respObj = new JSONObject(responseString);
                            String data = respObj.toString();
                            Log.d("LoginActivity","Data : " + data);
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                });
            }
            catch (Exception ex)
            {
                Toast toast = Toast.makeText(context, "ERROR", Toast.LENGTH_SHORT);
                toast.show();
            }
 */
