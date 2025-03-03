import java.util.Scanner;

public class BinaryChecker {
    public static boolean isBinary(String input) {
        return input.matches("[01]+"); // Hanya boleh berisi 0 dan 1
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Masukkan angka: ");
        String input = scanner.nextLine();

        if (isBinary(input)) {
            System.out.println(input + " adalah bilangan biner.");
        } else {
            System.out.println(input + " bukan bilangan biner.");
        }

        scanner.close();
    }
}