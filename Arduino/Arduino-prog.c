#include<ESP8266HTTPClient.h>
#include<ESP8266WiFi.h>
int button=D1;
int button1=D2;
const char* ssid=".......";
const char* passwd=".......";
void setup() {
    Serial,println("Serial commnication begin");
    pinMode(button,INPUT_PULLUP);
    pinMode(button1,INPUT_PULLUP);
    Serial.begin(9600);
    WiFi.begin(ssid,passwd);
    while(WiFi.status() != WL_CONNECTED);

    delay(1000);
    Serial.println("Connecting......")


}

void loop(){

    if(WiFi.status() == WL_CONNECTED)
    {
        HTTPClient http;
        WiFiClient client;
        if(digitalRead(button)==LOW)
        {
            http.begin(client,"http://192.168.43.230:5000/button1");
        }
        if(digitalRead(button1)==LOW)
        {
            http.begin(client,"http://192.168.43.230:5000/button2");
        }

        http.end();

    }

    delay(30000);

}