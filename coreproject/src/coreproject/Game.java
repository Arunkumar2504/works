package coreproject;

import java.util.*;

public class Game 
{
    
    public static final String R = "ROCK";
    public static final String P = "PAPER";
    public static final String S = "SCISSORS";

    public static void main(String args[]) 
    {
      System.out.println("Enter any one of the following inputs:  ");
      System.out.println("R-ROCK");
      System.out.println("P-PAPER");
      System.out.println("S-SCISSORS");
      System.out.println();
          
      String playerMove = getPlayerMove();
      String computerMove = getComputerMove(); 
 
      if (playerMove.equals(computerMove))
            System.out.println("Game is Tie !!");
               //ternary operator
      else if (playerMove.equals(Game.R))
        System.out.println(computerMove.equals(Game.P) ? "Computer Wins": "Player wins");   
      	
      else if (playerMove.equals(Game.P))
        System.out.println(computerMove.equals(Game.S) ? "Computer Wins": "Player wins");   
          
      else
        System.out.println(computerMove.equals(Game.R) ? "Computer Wins": "Player wins");   
    }
    
     
    public static String getComputerMove()
    {
        String computermove;
        Random random = new Random();
      int input = random.nextInt(3)+1;
        if (input == 1)
            computermove = Game.R;
        else if(input == 2)
            computermove = Game.P;
        else
            computermove = Game.S;
            
        System.out.println("Computer move is: " + computermove);
        System.out.println();
        return computermove;    
    }
    
    
    public static String getPlayerMove()
    {
        Scanner ob = new Scanner(System.in);
        String input = ob.next();
        String playermove = input.toUpperCase();
        System.out.println("Player move is: "+ playermove);
        return playermove;
    }    
}
