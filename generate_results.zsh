#!/bin/zsh

for i in 1 2 3 5
do
    echo "datasets/"$i"000/crescente.csv" > crescente$i 
    echo "datasets/"$i"000/decrescente.csv" > decrescente$i 
    echo "datasets/"$i"000/random.csv" > random$i 
    echo $i > op$i
    if [ $i -eq 5 ]
    then
        echo 4 > op$i
    fi
done

echo "Results of the algorithms" > result
echo >> result

for i in 1 2 3 5
do
    for j in 1 2 3 5
    do
        if [ $i -eq 1 ]
        then
            echo "Insertion Sort for array["$j"000]:" >> result
            echo >> result
        fi
        if [ $i -eq 2 ]
        then
            echo "Selection Sort for array["$j"000]:" >> result
            echo >> result
        fi
        if [ $i -eq 3 ]
        then
            echo "Merge Sort for array["$j"000]:" >> result
            echo >> result
        fi
        if [ $i -eq 5 ]
        then
            echo "Quick Sort for array["$j"000]:" >> result
            echo >> result
        fi
        
        echo "Increasing:" >> result
        python algord.py < crescente$i < op$j | tail -n 4 >> result
        echo "Decreasing:" >> result
        python algord.py < decrescente$i < op$j | tail -n 4 >> result
        echo "Random:" >> result
        python algord.py < random$i < op$j | tail -n 4 >> result
        echo "======================================================" >> result

    done
done

for i in 1 2 3 5
do
    rm crescente$i decrescente$i random$i op$i
done
