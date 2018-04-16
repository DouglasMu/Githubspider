
import jieba
from gensim import corpora
from gensim.similarities import Similarity
# 训练样本
raw_documents = [
    "Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"
]
corpora_documents = []
for item_text in raw_documents:
    item_str = list(jieba.cut(item_text))
    corpora_documents.append(item_str)

# 生成字典和向量语料
dictionary = corpora.Dictionary(corpora_documents)
corpus = [dictionary.doc2bow(text) for text in corpora_documents]

similarity = Similarity('-Similarity-index', corpus, num_features=400)

test_data_1 = 'Graph minors IV Widths of trees'
test_cut_raw_1 = list(jieba.cut(test_data_1))
print(test_cut_raw_1)
test_corpus_1 = dictionary.doc2bow(test_cut_raw_1)
similarity.num_best = 5
print(similarity[test_corpus_1])  # 返回最相似的样本材料,(index_of_document, similarity) tuples

