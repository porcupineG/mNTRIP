package com.mntripclient;

import com.google.android.maps.GeoPoint;
import com.google.android.maps.OverlayItem;

import android.location.Location;
import android.location.LocationListener;
import android.os.Bundle;

public class GPSPhoneListener implements LocationListener {

	private GeoPoint point;
	private GPSOPointOverlay gpsOverlay;
	
	public GPSPhoneListener(GPSOPointOverlay gpsOverlay) {
		this.gpsOverlay = gpsOverlay;
	}
	
	public void onLocationChanged(Location location) {
		point = new GeoPoint((int) (location.getLatitude() * 1000000.0), (int) (location.getLongitude() * 1000000.0));
		gpsOverlay.addUniqueOverlay(new OverlayItem(point, "GPSP", ""));
		FileLog.getInstance().log("GPSP " + location.getTime() + " " + location.getLatitude() + " " + location.getLatitude() + "\r\n");
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
