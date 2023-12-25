import java.time.Duration;
import java.time.Instant;

public class MillionCountSpeedTestInJava {
  public static void main(String[] args) {
    int i = 0;
    Instant inst1 = Instant.now();
    while (i < 1000000000) {
      i++;
    }
    Instant inst2 = Instant.now();
    System.out.println("Elapsed Time: " + Duration.between(inst1, inst2).toString());
  }
}
