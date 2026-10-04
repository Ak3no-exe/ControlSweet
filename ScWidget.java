package com.sweetcontrol.app;

import android.app.PendingIntent;
import android.appwidget.AppWidgetManager;
import android.appwidget.AppWidgetProvider;
import android.content.Context;
import android.content.Intent;
import android.widget.RemoteViews;
import org.json.JSONArray;
import org.json.JSONObject;

public class ScWidget extends AppWidgetProvider {
    @Override
    public void onUpdate(Context c, AppWidgetManager m, int[] ids) {
        String txt = "Ouvre l'appli pour charger les rangs";
        try {
            String raw = c.getSharedPreferences("CapacitorStorage", Context.MODE_PRIVATE)
                          .getString("sc_widget", null);
            if (raw != null) {
                JSONArray a = new JSONObject(raw).getJSONArray("lines");
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < a.length(); i++) {
                    if (i > 0) sb.append("\n");
                    sb.append(a.getString(i));
                }
                if (sb.length() > 0) txt = sb.toString();
            }
        } catch (Exception ignored) {}

        Intent open = c.getPackageManager().getLaunchIntentForPackage(c.getPackageName());
        PendingIntent pi = PendingIntent.getActivity(c, 0, open, PendingIntent.FLAG_IMMUTABLE);
        for (int id : ids) {
            RemoteViews v = new RemoteViews(c.getPackageName(), R.layout.sc_widget);
            v.setTextViewText(R.id.body, txt);
            v.setOnClickPendingIntent(R.id.root, pi);
            m.updateAppWidget(id, v);
        }
    }
}
