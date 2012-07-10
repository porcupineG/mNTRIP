package com.example.android.apis.view;

import com.google.android.maps.GeoPoint;
import com.google.android.maps.OverlayItem;

import android.annotation.SuppressLint;
import android.location.Location;
import android.location.LocationListener;
import android.os.Bundle;
import android.util.Log;

@SuppressLint("ParserError")
public class GPSPhoneListener implements LocationListener {

	private final GPSOverlay gpsOverlay;

	public GPSPhoneListener(GPSOverlay gpsOverlay) {
		this.gpsOverlay = gpsOverlay;
	}

	@SuppressLint("ParserError")
	public void onLocationChanged(Location location) {
		GeoPoint point = new GeoPoint((int) (location.getLatitude() * 1000000.0), (int) (location.getLongitude() * 1000000.0));
		gpsOverlay.addOverlay(new OverlayItem(point, "asd", "asd"));
		Log.d("GPSPhoneListener", location.getLatitude() + " " + location.getLongitude());

	}

	public void onProviderDisabled(String provider) {
		// TODO Auto-generated method stub

	}

	public void onProviderEnabled(String provider) {
		// TODO Auto-generated method stub

	}

	public void onStatusChanged(String provider, int status, Bundle extras) {
		// TODO Auto-generated method stub

	}

}
