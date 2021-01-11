class power : public Component {
 public:
    void setup() override {
        pinMode(13, OUTPUT);
        digitalWrite(13, LOW);
        ESP_LOGD("power", "The GPIO pin 13 is LOW -> power on !");
    }

    float get_setup_priority() const override {
        auto tmp = esphome::setup_priority::BUS;
        ESP_LOGD("power", "priority is: %d", tmp);
        return tmp;
    }

    void on_safe_shutdown() const {
        digitalWrite(13, HIGH);
        ESP_LOGD("power", "The GPIO pin 13 is HIGH -> power off !");
    }
};
