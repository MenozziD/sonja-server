#git init
#git add *
#git commit -m "UP"   
#git pull origin master --allow-unrelated-histories
#git fetch origin master
#git push origin master --allow-unrelated-histories
#if [[ ! $1 ]];
#then
# echo "Branch vuota o non valida!"
# exit
#fi

git branch > branch.tmp
branch=$(cat branch.tmp | grep '*')
branch=${branch:2}

commit="New commit"
#dt=$(date)




git init
git fetch origin "$branch"
git pull origin "$branch"
git add *
if [[ $1 ]];
then
 commit=$1
fi
git commit -m "$commit $dt"
git push https://VanMenoz92:git3553@github.com/VanMenoz92/BotSonja.git "$branch" 
