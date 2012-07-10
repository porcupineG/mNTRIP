package com.example.android.apis.view;

import java.util.ArrayList;

import android.annotation.SuppressLint;
import android.graphics.drawable.Drawable;

import com.google.android.maps.GeoPoint;
import com.google.android.maps.ItemizedOverlay;
import com.google.android.maps.OverlayItem;

@SuppressLint("ParserError")
public class GPSOverlay extends ItemizedOverlay<OverlayItem> {

	private ArrayList<OverlayItem> overlays = new ArrayList<OverlayItem>();
	
	public GPSOverlay(Drawable defaultMarker) {
		super(boundCenterBottom(defaultMarker));
		GeoPoint point = new GeoPoint(19240000,-99120000);
		OverlayItem overlayItem = new OverlayItem(point, "chuj", "dupa");
		addOverlay(overlayItem);
		
	}

	public void addOverlay(OverlayItem overlay) {
	    overlays.add(overlay);
	    populate();
	}
	
	@Override
	protected OverlayItem createItem(int i) {
		return overlays.get(i);
	}

	@Override
	public int size() {
		// TODO Auto-generated method stub
		return overlays.size();
	}

}
