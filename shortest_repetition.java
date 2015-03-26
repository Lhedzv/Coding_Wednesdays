import java.io.*;

public class Main {

    public static void main (String[] args) throws IOException {

        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null){
            line = line.trim();

            getShortestRepetition(line);

            }
        }

    public static void getShortestRepetition(String line){

        int string_len = line.length();
        int shortest_repetition_len = string_len;
        int start = string_len/2;

        z:for (int i = start; i > 0 ; i--) {

            if(string_len%i == 0) {

                int current_max_repetitions = string_len / i;
                int check_pattern = 1;

                y:for (int j = 1; j < current_max_repetitions; j++) {

                    if (!line.substring(0, i).equals(line.substring(i * j, (i * j) + i))) {
                        break y;
                    } else {
                        check_pattern++;
                    }
                }

                if (check_pattern == current_max_repetitions) {
                    shortest_repetition_len = i;
                }

            }

        }
        System.out.println(shortest_repetition_len);


    }
    
    }


