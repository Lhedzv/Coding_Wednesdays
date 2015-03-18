import java.io.*;

/**
 * Created by CSI - Pro on 3/11/2015.
 */
public class Main
{

        public static void main (String[] args) throws IOException {
            File file = new File(args[0]);
            BufferedReader buffer = new BufferedReader(new FileReader(file));
            String line;
            while ((line = buffer.readLine()) != null) {
                line = line.trim();
                removeCharacters(line);
            }
        }


    public static void removeCharacters(String Line){

        String[] Line_Splitted = Line.split(",");
        String[] Sentence = Line_Splitted[0].trim().split("");
        String[] Letters = Line_Splitted[1].trim().split("");
        
        String result = "";
        int checked_letters = 0;

        z:for(String letter : Sentence) {

            x:for (String constrain : Letters) {

                if(constrain.equals(letter)){
                    break x;
                }else{
                    checked_letters += 1;
                }

            }


            if(checked_letters == Letters.length){ result += letter;}
            checked_letters = 0;
        }

        System.out.println(result);


    }




}