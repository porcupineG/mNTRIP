package com.example.android.apis.view;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.Arrays;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Future;

import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.params.HttpConnectionParams;

import android.net.http.AndroidHttpClient;
import android.util.Log;

public class NTRIPCasterDownloadTask implements Runnable {

	private final ExecutorService httpExecutorService;
	private AndroidHttpClient httpClient;
	private URI uri;

	public NTRIPCasterDownloadTask(ExecutorService httpExecutorService) {
		this.httpExecutorService = httpExecutorService;
		httpClient = AndroidHttpClient.newInstance("NTRIPCaster");
		
		HttpConnectionParams.setTcpNoDelay(httpClient.getParams(), true);
		HttpConnectionParams.setSoTimeout(httpClient.getParams(), 500);
		
		try {
			uri = new URI("http://wp.pl");
//			uri = new URI("http://spierdalaj.org/");
		} catch (URISyntaxException e) {
			e.printStackTrace();
		}		
	}

	public void run() {
		HttpGet request = new HttpGet();
		Log.d("NTRIPCasterDownloadTask", "runTop");
		try {
			request.setURI(uri);
			HttpResponse response = httpClient.execute(request);
			long length = response.getEntity().getContentLength();
			byte [] resBytes = new byte[(int) length];
			response.getEntity().getContent().read(resBytes);
			Log.d("NTRIPCasterDownloadTask", new String(resBytes));
			
			
		} catch (Exception e) {
			Log.e("NTRIPCasterDownloadTask", e.getMessage(), e);
		}
	
		Future<?> future = httpExecutorService.submit(this);
		//future.ge
		
	}

}
