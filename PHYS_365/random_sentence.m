% Creates cell arrays of names, verbs, and nouns. Then prints a sentence
% formed from a random chaice in each of the arrays.
names = {'Harry','Xavier', 'Sue'};
verbs = {'loves','eats'};
nouns = {'baseballs','rocks','sushi'};
rand_name = randi(length(names),1);
rand_verb = randi(length(verbs),1);
rand_noun = randi(length(nouns),1);
fprintf('%s %s %s.\n',names{rand_name},verbs{rand_verb},nouns{rand_noun})