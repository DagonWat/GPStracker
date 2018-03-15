package com.yayandroid.locationmanager.configuration;

import android.Manifest;

import com.google.android.gms.location.LocationRequest;

public final class Defaults {

    private static final int SECOND = 1000;
    private static final int MINUTE = 60 * SECOND;

    static final int WAIT_PERIOD = 10 * SECOND;
    static final int TIME_PERIOD = SECOND * 20;

    static final int LOCATION_DISTANCE_INTERVAL = 0;
    static final int LOCATION_INTERVAL = SECOND * 20;

    static final float MIN_ACCURACY = 4.0f;

    static final boolean KEEP_TRACKING = true;
    static final boolean FALLBACK_TO_DEFAULT = true;
    static final boolean ASK_FOR_GP_SERVICES = true;
    static final boolean ASK_FOR_SETTINGS_API = true;
    static final boolean FAIL_ON_CONNECTION_SUSPENDED = true;
    static final boolean FAIL_ON_SETTINGS_API_SUSPENDED = false;
    static final boolean IGNORE_LAST_KNOW_LOCATION = false;
    static final int SUSPENDED_CONNECTION_RETRY_COUNT = 2;

    static final String EMPTY_STRING = "";
    public static final String[] LOCATION_PERMISSIONS = new String[] { Manifest.permission.ACCESS_COARSE_LOCATION,
          Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.WRITE_EXTERNAL_STORAGE };

    private static final int LOCATION_PRIORITY = LocationRequest.PRIORITY_BALANCED_POWER_ACCURACY;
    private static final int LOCATION_FASTEST_INTERVAL = MINUTE;

    /**
     * https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest
     */
    public static LocationRequest createDefaultLocationRequest() {
        return LocationRequest.create()
              .setPriority(Defaults.LOCATION_PRIORITY)
              .setInterval(Defaults.LOCATION_INTERVAL)
              .setFastestInterval(Defaults.LOCATION_FASTEST_INTERVAL);
    }

    private Defaults() {
        // No instance
    }

}
