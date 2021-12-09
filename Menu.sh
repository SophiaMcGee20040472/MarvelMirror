PS3="Please enter one of the numbers above:" 
echo -e "\e[1;35m Welcome...... \e[0m \e[1;35m" 
echo -e "\e[1;35m Please choose one of the following: \e[0m"

# Have chosen white for menu as it is very clean and clear colour opposed to grey
echo -e "\e[1;32m \e[0m \e[1;29m"
echo "--------------------------------------------------------------------------------"

options=("Run Marvel Mirror APP      " "livestream" "Quit" )

select opt in "${options[@]}"
do
    case $opt in
        "Run Marvel Mirror APP      ")
            echo
            # entering option input into greeting
            echo -e "\e[1;35m You Chose $opt ---------> \e[0m" 
            echo
            exec python3 ./Blynkmirror.py & exec python3 livestream.py
            ;;
        "Quit")
            echo "--------------------------------------------------------------------------------"
            echo "You chose to exit."
            echo 
            echo "Have a nice day Bye!"
            echo "--------------------------------------------------------------------------------"
            break
            sleep 1
            ;;
        *) echo "invalid option $REPLY";;
    esac

done

