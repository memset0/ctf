import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.*;

class BasicRe2 {
  public static void main(String args[]) {
    BasicRe2 basicRe2 = new BasicRe2();
    Scanner scanner = new Scanner(System.in);
    System.out.println("Password please:");
    // String userInput = scanner.next();
    String userInput = "abcdefghijklnmopqrstuvwxyz123123";
    if (basicRe2.checkPassword(userInput)) {
      System.out.println("Congratulations!");
    } else {
      System.out.println("Try harder.");
    }
    scanner.close();
  }

  // Each character can be represented as a byte value using its
  // ASCII encoding. Each byte contains 8 bits, and an int contains
  // 32 bits, so we can "pack" 4 bytes into a single int. Here's an
  // example: if the hex string is "01ab", then those can be
  // represented as the bytes {0x30, 0x31, 0x61, 0x62}. When those
  // bytes are represented as binary, they are:
  //
  // 0x30: 00110000
  // 0x31: 00110001
  // 0x61: 01100001
  // 0x62: 01100010
  //
  // If we put those 4 binary numbers end to end, we end up with 32
  // bits that can be interpreted as an int.
  //
  // 00110000001100010110000101100010 -> 808542562
  //
  // Since 4 chars can be represented as 1 int, the 32 character password can
  // be represented as an array of 8 ints.
  //
  // - Minion #7816
  public int[] passwordToIntArray(String hex) {
    int[] x = new int[8];
    byte[] hexBytes = hex.getBytes();
    for (int i = 0; i < 32; i++) {
      System.out.println(hexBytes[i]);
    }
    for (int i = 0; i < 8; i++) {
      x[i] = hexBytes[i * 4] << 24 | hexBytes[i * 4 + 1] << 16 | hexBytes[i * 4 + 2] << 8 | hexBytes[i * 4 + 3];
    }
    return x;
  }

  public boolean checkPassword(String password) {
    if (password.length() != 32) {
      return false;
    }
    int[] x = passwordToIntArray(password);
    // for (int i = 0; i < 8; i++) {
    //   System.out.print((x[i]) & ((1 << 8) - 1));
    //   System.out.print(' ');
    //   System.out.print((x[i] >> 8) & ((1 << 8) - 1));
    //   System.out.print(' ');
    //   System.out.print((x[i] >> 16) & ((1 << 8) - 1));
    //   System.out.print(' ');
    //   System.out.print((x[i] >> 24) & ((1 << 8) - 1));
    //   System.out.print(' ');
    //   System.out.println(x[i]);
    // }
    return x[0] == 1211396208 && x[1] == 2034593380 && x[2] == 1765043792 && x[3] == 878930775 && x[4] == 1769236560
        && x[5] == 2037672047 && x[6] == 1851749236 && x[7] == 1920295796;
  }
}