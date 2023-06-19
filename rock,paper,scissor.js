const intgame=()=>{
    const startgame=confirm("shall we play the game");
    startgame? playgame():alert("may be next time");
};
const playgame=()=>{
    while(true){
        let playerchoice=getplayerchoice();
        playerchoice=formatplayerchioice
        (playerchoice);
        if(playerchoice===""){
            invalidchoice();
            continue;
        }
        if(!playerchoice){
            decidednottoplay();
            break;
        }
        playerchoice=evaluateplayerchoice(playerchoice);
        if(!playerchoice)
        {
            invalidchoice();
            continue;
        }
        const computerchoice=getcomputerchoice();
        const result=determinewinner(playerchoice,computerchoice);
        displayresult(result);
        if(asktoplayagain()){
            continue;
        }else{
            thanksforplaying();
            break;
        }
    }
};

const getplayerchoice=()=>{
    return prompt("please enter the rock,paper,scissor");
};
const formatplayerchioice=(playerchoice)=>{
    if(playerchoice || playerchoice==="")
    {
        return playerchoice.trim().toLowerCase();
    }
    else{
        return false;
    }
};
const decidednottoplay=()=>{
    alert("i gusses u changed ur mind");
};

const evaluateplayerchoice=(playerchoice)=>{
    if(playerOne==="rock"
    ||playerOne ==="paper"
    ||playerOne==="scissor"){
        return playerchoice;
    }
    else{
        return false;
    }

};
const invalidchoice=()=>{
    const randomnumber=Math.floor(Math.random()*3);
    const key=["rock","paper","scissor"];
    return key[randomnumber];


}
const determinewinner=(playerOne,computer)=>{
const winner=playerOne===computer?
"tie game":playerOne==="rock"&& computer==="paper"?`playerOne:${playerOne}\n computer:${computer}\n computer wins!`
:playerOne==="paper"&&computer==="scissor"
?`playerOne:${playerOne}\ncomputer:${computer}\n computer wins!`
:playerOne==="scissors"&& computer=="rock"?`playerOne:${playerOne}\ncomputer:${computer}\n computer wins!`
:`playerOne:${playerOne}\ncomputer:${computer}\nplayer wins!`;
alert(result);
let playagain=confirm("play again");
playagain?location.reload():alert("okay thank u ");
return winner;
};
const displayresult=(result)=>{
    alert(result);
};
const asktoplayagain=()=>{
    return confirm("play again?")
};
const thanksforplaying=()=>{
    alert("ok, thanks for playing")
};
intgame();
 
