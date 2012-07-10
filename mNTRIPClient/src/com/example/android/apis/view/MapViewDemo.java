/*
 * Copyright (C) 2007 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.android.apis.view;

import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import com.example.android.google.apis.R;
import com.google.android.maps.MapActivity;
import com.google.android.maps.MapView;
import com.google.android.maps.Overlay;

import android.annotation.SuppressLint;
import android.graphics.drawable.Drawable;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;

/**
 * Example of how to use an {@link com.google.android.maps.MapView}.
 * <h3>MapViewDemo</h3>

<p>This demonstrates creating a Map based Activity.</p>

<h4>Demo</h4>
Views/MapView

<h4>Source files</h4>
 * <table class="LinkTable">
 *         <tr>
 *             <td >src/com.example.android.apis/view/MapViewDemo.java</td>
 *             <td >The Alert Dialog Samples implementation</td>
 *         </tr>
 *         <tr>
 *             <td >/res/layout/mapview.xml</td>
 *             <td >Defines contents of the screen</td>
 *         </tr>
 * </table>
 */
@SuppressLint({ "ParserError", "ParserError", "ParserError", "ParserError", "ParserError" })
public class MapViewDemo extends MapActivity {

    private LocationManager locationManager;
	private ExecutorService httpExecutorService;

	
	
	@Override
	protected void onDestroy() {
		super.onDestroy();
		
		httpExecutorService.shutdown();
	}

	@Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.mapview);

        MapView mapView = (MapView) findViewById(R.id.mapView);
        
        List<Overlay> mapOverlays = mapView.getOverlays();
        
        Drawable drawable = this.getResources().getDrawable(R.drawable.app_sample_code);
        
        GPSOverlay gpsOverlay = new GPSOverlay(drawable);
		mapOverlays.add(gpsOverlay);
        
        subcribeForGPSUpdate(gpsOverlay);
        
        initHTTPThread();
        
    }

    private void initHTTPThread() {
    	httpExecutorService = Executors.newSingleThreadExecutor();
    	httpExecutorService.execute(new NTRIPCasterDownloadTask(httpExecutorService));
	}

	@SuppressLint({ "ParserError", "ParserError" })
	private void subcribeForGPSUpdate(GPSOverlay gpsOverlay) {
		locationManager = (LocationManager) getSystemService(LOCATION_SERVICE);
		locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, new GPSPhoneListener(gpsOverlay));
	}

	@Override
    protected boolean isRouteDisplayed() { return false; }
}
