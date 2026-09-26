#define RED_PIN    2
#define GREEN_PIN  4
#define BLUE_PIN   5

String message = "";

void setColor(String bits)
{
  digitalWrite(RED_PIN, LOW);
  digitalWrite(GREEN_PIN, LOW);
  digitalWrite(BLUE_PIN, LOW);

  if(bits == "00")
  {
    digitalWrite(RED_PIN, HIGH);
  }
  else if(bits == "01")
  {
    digitalWrite(GREEN_PIN, HIGH);
  }
  else if(bits == "10")
  {
    digitalWrite(BLUE_PIN, HIGH);
  }
else if(bits == "11")
{
  digitalWrite(RED_PIN, HIGH);
  digitalWrite(GREEN_PIN, HIGH);
  digitalWrite(BLUE_PIN, LOW);
}

    delay(1000);   // show each color for 1 second

  digitalWrite(RED_PIN, LOW);
  digitalWrite(GREEN_PIN, LOW);
  digitalWrite(BLUE_PIN, LOW);

  delay(150);
}

void transmitCharacter(char c)
{
  byte value = (byte)c;

  String binaryString = "";

  for(int i = 7; i >= 0; i--)
  {
    binaryString += String((value >> i) & 1);
  }

  Serial.print(c);
  Serial.print(" -> ");
  Serial.println(binaryString);

  for(int i = 0; i < 8; i += 2)
  {
    String twoBits = binaryString.substring(i, i + 2);
    setColor(twoBits);
  }
}

void setup()
{
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);

  Serial.begin(115200);

  Serial.println("Enter Message:");
}

void loop()
{
  if(Serial.available())
  {
    message = Serial.readStringUntil('\n');
    message.trim();

    Serial.print("Sending: ");
    Serial.println(message);

    for(int i = 0; i < message.length(); i++)
    {
      transmitCharacter(message[i]);
    }

    Serial.println("Transmission Complete");
    Serial.println("Enter New Message:");
  }
}