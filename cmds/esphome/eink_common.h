#include <string>
#include <iostream>
#include <sstream>
#include <ArduinoJson.h>

// Conditions
#define ICON_w_clear_night "\U000F0594"
#define ICON_w_cloudy "\U000F0590"
#define ICON_w_fog "\U000F0591"
#define ICON_w_hail "\U000F0592"
#define ICON_w_lightning "\U000F0593"
#define ICON_w_lightning_rainy "\U000F067E"
#define ICON_w_night_partly_cloudy "\U000F0F31"
#define ICON_w_partly_cloudy "\U000F0595"
#define ICON_w_pouring "\U000F0596"
#define ICON_w_rainy "\U000F0597"
#define ICON_w_snowy "\U000F0F36"
#define ICON_w_snowy_rainy "\U000F067F"
#define ICON_w_sunny "\U000F0599"
#define ICON_w_windy "\U000F059D"
#define ICON_w_windy_variant "\U000F059E"
#define ICON_w_exceptional "\U000F0F38"

// Battery
#define ICON_bat_empty	"\U000F10CD"
#define ICON_bat_10	"\U000F007A"
#define ICON_bat_20	"\U000F007B"
#define ICON_bat_30	"\U000F007C"
#define ICON_bat_40	"\U000F007D"
#define ICON_bat_50	"\U000F007E"
#define ICON_bat_60	"\U000F007F"
#define ICON_bat_70	"\U000F0080"
#define ICON_bat_80	"\U000F0081"
#define ICON_bat_90	"\U000F0082"
#define ICON_bat_100	"\U000F0079"

// icon constants
#define ICON_temp_high        "\U000F10C2"
#define ICON_temp_low         "\U000F10C3"
#define ICON_rain             "\U000F067F"
#define ICON_sofa             "\U000F04B9"
#define ICON_shower           "\U000F09A1"
#define ICON_chair            "\U000F0F48"
#define ICON_bed              "\U000F0FD2"
#define ICON_up               "\U000F005E"
#define ICON_down             "\U000F0046"
#define ICON_sun              "\U000F0599"
#define ICON_sun_down         "\U000F059B"
#define ICON_sun_up           "\U000F059C"
#define ICON_water_boiler     "\U000F0F92"
#define ICON_heat_pump        "\U000F1A44"
#define ICON_shutter_alert    "\U000F111D"
#define ICON_power            "\U000F192D"
#define ICON_water            "\U000F1B29"
#define ICON_gauge            "\U000F029A"
#define ICON_trend_up         "\U000F0535"
#define ICON_trend_no         "\U000F0534"
#define ICON_trend_down       "\U000F0533"
#define ICON_wind             "\U000F1B5A"
#define ICON_wind_alt         "\U000F15FA"
#define ICON_drop             "\U000F0E0A"
#define ICON_wind_se          "\U000F19B4"
#define ICON_wind_sw          "\U000F19B5"
#define ICON_wind_nw          "\U000F19B7"
#define ICON_wind_ne          "\U000F19B6"
#define ICON_wind_w           "\U000F19B0"
#define ICON_wind_e           "\U000F19B1"
#define ICON_wind_s           "\U000F19B3"
#define ICON_wind_n           "\U000F19B2"
#define ICON_temp             "\U000F050F"
#define ICON_fan_auto         "\U000F171D"
#define ICON_cpu_usage        "\U000F0EE0"
#define ICON_cpu_temp         "\U000F0FF8"
#define ICON_mem              "\U000F035B"
#define ICON_disk             "\U000F02CA"
#define ICON_ping             "\U000F01E7"
#define ICON_net_disk         "\U000F12D6"
#define ICON_meter_electric   "\U000F1A58"
#define ICON_heat_coil        "\U000F1AAF"
#define ICON_wind_turbine     "\U000F0DA5"
#define ICON_lightning_bolt   "\U000F140C"
#define ICON_sleep_off        "\U000F04B3"
#define ICON_temp_out         "\U000F0F35"
#define ICON_clouds           "\U000F1B95"
#define ICON_rain_alt         "\U000F0596"
#define ICON_rain_prob        "\U000F1A36"
#define ICON_sleep            "\U000F04B2"
#define ICON_wifi_alert       "\U000F0920"
#define ICON_windy            "\U000F059D"
#define ICON_ota              "\U000F06B0"
#define ICON_download         "\U000F0997"
#define ICON_timer            "\U000F051F"
#define ICON_wash             "\U000F072A"
#define ICON_bank             "\U000F0070"

// positioning constants
#define xRes 800
#define yRes 480
#define xCenter (xRes/2 + 100) // X position center
#define pad 10
#define celsiusSuperscript 12
#define rowHeight 45
#define temperatureCol 195
#define humidityCol 300
#define weatherCol 80
#define weatherRow 260
#define weatherrowHeight 36
#define weatherTempCorr 15
#define weatherAttrCol0 0
#define weatherAttrCol1 440
#define weatherAttrRow 86
#define weatherAttrYstep 32
#define iconPad (36)
#define rownSpace (24)
#define tabelStartX (62)
#define tabelStepX (60)
#define tabelStartY (370)
#define tabelStepY (36)
#define tableRowiconX (10)

ESPTime str2dt(std::string s)
{
  struct tm timeParsed;
  strptime(s.c_str(), "%Y-%m-%dT%H:%M:%S", &timeParsed);
  // time_t c_time = mktime(&timeParsed);
  time_t c_time = mktime(&timeParsed);
  c_time += ESPTime::timezone_offset();
  return ESPTime::from_epoch_local(c_time);
}

bool in_range(float min, float val, float max)
{
  return (min <= val) && (val <= max);
}

std::string conditionToIcon(std::string condition, bool daytime)
{
  if (condition == "clear-night") return ICON_w_clear_night;
  if (condition == "cloudy") return ICON_w_cloudy;
  if (condition == "fog") return ICON_w_fog;
  if (condition == "hail") return ICON_w_hail;
  if (condition == "lightning") return ICON_w_lightning;
  if (condition == "lightning-rainy") return ICON_w_lightning_rainy;
  if (condition == "partlycloudy" && !daytime) return ICON_w_night_partly_cloudy;
  if (condition == "partlycloudy" && daytime) return ICON_w_partly_cloudy;
  if (condition == "pouring") return ICON_w_pouring;
  if (condition == "rainy") return ICON_w_rainy;
  if (condition == "snowy") return ICON_w_snowy;
  if (condition == "snowy-rainy") return ICON_w_snowy_rainy;
  if (condition == "sunny") return ICON_w_sunny;
  if (condition == "windy") return ICON_w_windy;
  if (condition == "windy-variant") return ICON_w_windy_variant;
  if (condition == "exceptional") return ICON_w_exceptional;
  return "";
}

std::string notificationIcon(std::string icon)
{
  std::string ret = "\U000F002A"; // alert-outline
  if (icon == "window-shutter-alert")             ret = "\U000F111D";
  else if (icon == "restart-alert")               ret = "\U000F110C";
  else if (icon == "router-network-wireless")     ret = "\U000F1C97";
  else if (icon == "trending-up")                 ret = "\U000F0535";
  else if (icon == "trending-down")               ret = "\U000F0533";
  else if (icon == "trending-neutral")            ret = "\U000F0534";
  else if (icon == "weather-cloudy-alert")        ret = "\U000F0F2F";
  else if (icon == "record-rec")                  ret = "\U000F044B";
  else if (icon == "kodi")                        ret = "\U000F0314";
  else if (icon == "television")                  ret = "\U000F0502";
  else if (icon == "download-outline")            ret = "\U000F0B8F";
  else if (icon == "subtitles-outline")           ret = "\U000F0A17";
  else if (icon == "door")                        ret = "\U000F081A";
  else if (icon == "connection")                  ret = "\U000F1616";
  else if (icon == "update")                      ret = "\U000F06B0";
  else if (icon == "pipe")                        ret = "\U000F07E5";
  else if (icon == "pipe-disconnected")           ret = "\U000F07E6";
  else if (icon == "home-lightning-bolt-outline") ret = "\U000F1904";
  else if (icon == "home-outline")                ret = "\U000F06A1";
  else if (icon == "door-closed")                 ret = "\U000F081B";
  else if (icon == "robot-vacuum")                ret = "\U000F070D";
  else if (icon == "alert-octagon-outline")       ret = "\U000F0CE6";

  return ret;
}

std::string batteryToIcon(float battery)
{
  if (battery > 90) return ICON_bat_100;
  if (battery > 80) return ICON_bat_90;
  if (battery > 70) return ICON_bat_80;
  if (battery > 60) return ICON_bat_70;
  if (battery > 50) return ICON_bat_60;
  if (battery > 40) return ICON_bat_50;
  if (battery > 30) return ICON_bat_40;
  if (battery > 20) return ICON_bat_30;
  if (battery > 10) return ICON_bat_20;
  if (battery > 0) return ICON_bat_10;
  return ICON_bat_empty;
}
