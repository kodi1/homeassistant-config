# -*- coding: utf-8 -*-

import sys
import os
import requests as rq
import json
import re

def fetch_data(f):
  try:
    d = {}
    r = rq.get(f)
    for k in _data_re:
      m = re.search(k['re'], r.text, (re.IGNORECASE | re.MULTILINE | re.DOTALL))
      if m:
        d[k['name']] = m.group(1)
        if k['name'] == 'uptime':
          n = re.search(r'(\d+).*?(\d+).*?(\d+)', m.group(1), (re.IGNORECASE | re.MULTILINE | re.DOTALL))
          if n:
            d['mtime'] = int(n.group(1)) * 60 * 24 + int(n.group(2)) * 60 + int(n.group(3))
    return d
  except:
    pass
  return None

_data_re = [
    {'re': r'uptime:<td>(.*?)<tr>', 'name': 'uptime'},
    {'re': r'load.*?(\d+)', 'name': 'load'},
    {'re': r'rssi.*?(\d+)', 'name': 'rssi'},
    {'re': r'Boot\ cause:<td>(.*?)<tr>', 'name': 'boot_cause'},
    {'re': r'Boot\ count.*?(\d+)', 'name': 'boot_count'},
  ]

if __name__ == '__main__':
  if len(sys.argv) == 1:
    print ('Usage %s http://esp_easy_mega_url:esp_port/sysinfo' % sys.argv[0])
    sys.exit(1)
  print ('Url: %s' % sys.argv[1])
  print (fetch_data(sys.argv[1]))
  sys.exit(0)
else:
  import voluptuous as vol
  from datetime import timedelta
  from homeassistant.components.binary_sensor import BinarySensorDevice
  import homeassistant.helpers.config_validation as cv
  from homeassistant.components.sensor import PLATFORM_SCHEMA
  from homeassistant.const import (
          CONF_HOST, CONF_NAME,
  )

  SCAN_INTERVAL = timedelta(seconds=60)

  PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
          vol.Required(CONF_HOST): cv.string,
          vol.Required(CONF_NAME): cv.string,
  })

  def setup_platform(hass, config, add_devices, discovery_info=None):
      """Setup the sensor platform."""
      host = config.get(CONF_HOST)
      name = config.get(CONF_NAME)
      add_devices([EspSensor(host, name, 'connectivity')], True)

  class EspSensor(BinarySensorDevice):
      """Representation of a Sensor."""
      def __init__(self, host, name, device_type):
          """Initialize the sensor."""
          self._host = host
          self._fetch = fetch_data
          self._name = name
          self._type = device_type
          self._data = self._fetch(self._host)
          self._state = False

      @property
      def device_class(self):
          """Return the class of this sensor."""
          return self._type

      @property
      def should_poll(self):
          """Polling needed for a demo binary sensor."""
          return True

      @property
      def name(self):
          """Return the name of the binary sensor."""
          return self._name

      @property
      def device_state_attributes(self):
        """Return the state attributes of the sensor."""
        if self._data:
          return self._data
        else:
          return None

      @property
      def is_on(self):
          """Return true if the binary sensor is on."""
          return self._state

      def update(self):
          """Fetch new state data for the sensor.
          This is the only method that should fetch new data for Home Assistant.
          """
          self._data = self._fetch(self._host)
          if self._data:
            self._state = True
          else:
            self._state = False
