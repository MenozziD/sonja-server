#! /bin/bash
ver="1.0.1"
path='python /home/pi/Desktop/BotSonja/bot.py'

cd /home/pi/Desktop/BotSonja

if [ "$1" == "start" ];
then
 processId=$(ps -ef | grep 'bot.py' | grep -v 'grep' | awk '{ printf $2 }')
 if [[ $processId ]];
 then
  echo "bot gia' attivo!"	
 else
  if [ "$2" != "lx" ];
  then
   #python ../bot.py &
   python /home/pi/Desktop/BotSonja/bot.py &
  else
   lxterminal -t "botSonja" -e bash -c "$path"
  fi
  sleep 1
  processId=$(ps -ef | grep 'bot.py' | grep -v 'grep' | awk '{ printf $2 }') 
  if [[ $processId ]];	
  then
   echo "bot START"
  else
   echo "bot ERRORE: Il comando python non ha avviato il processo!"
   exit	
  fi
 fi
fi

if [ "$1" == "stop" ];
then
 processId=$(ps -ef | grep 'bot.py' | grep -v 'grep' | awk '{ printf $2 }')
 if [[ $processId ]];
 then
  sudo kill $processId
  processId=$(ps -ef | grep 'bot.py' | grep -v 'grep' | awk '{ printf $2 }')
  if [[ $processId ]];	
  then
   echo "bot ERRORE: Il comando kill non ha fermato il processo!"
   exit	
  else
   echo "bot STOP"
  fi
 else
  echo "bot non attivo!"	
 fi
fi

if [ "$1" == "pid" ];
then
 processId=$(ps -ef | grep 'bot.py' | grep -v 'grep' | awk '{ printf $2 }')
 echo "bot PID:" $processId	
fi

if [ "$1" == "status" ];
then
 processId=$(ps -ef | grep 'bot.py' | grep -v 'grep' | awk '{ printf $2 }')
 if [[ $processId ]];
 then
  echo "bot ON "
 else
  echo "bot OFF"
 fi
fi

if [ "$1" == "restart" ];
then
 processId=$(ps -ef | grep 'bot.py' | grep -v 'grep' | awk '{ printf $2 }')
 if [[ $processId ]];
 then
  echo "bot PID:" $processId
  sudo kill $processId
  processId=$(ps -ef | grep 'bot.py' | grep -v 'grep' | awk '{ printf $2 }')
  if [[ $processId ]];	
  then
   echo "bot ERRORE: Il comando kill non ha fermato il processo!"
   exit	
  else
   echo "bot STOP"
  fi
  if [ "$2" != "lx" ];
  then
   python /home/pi/Desktop/BotSonja/bot.py &
  else
   lxterminal -t "botSonja" -e bash -c "$path"
  fi
  sleep 1
  processId=$(ps -ef | grep 'bot.py' | grep -v 'grep' | awk '{ printf $2 }')
  if [[ $processId ]];	
  then
   echo "bot RESTART"
  else
   echo "bot ERRORE: Il comando python non ha avviato il processo!"
   exit	
  fi
 fi
fi

if [ "$1" == "version" ];
then
 echo "botcmd " $ver
fi



if [ "$1" == "help" ];
then
 echo "Elenco Comandi: "
 echo "pid		-- Ritorna PID processo del bot"
 echo "status		-- Indica stato bot ON/OFF e PID"
 echo "stop		-- Termina l'esecuzione del bot"
 echo "start		-- Avvia l'esecuzione del bot"
 echo "restart		-- Riavvia l'esecuzione del bot"
 echo "help		-- Mostra elenco comandi script"
 echo "version		-- Mostra versione script"
fi

