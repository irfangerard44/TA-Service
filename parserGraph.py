class parserDftoGraph:
    def __init__(self, data):
        self.data = data
    def parse(self):
        cluster = []
        clusters = []
        result = []
        edges = []
        for index, row in self.data.iterrows():
            id = row['id']
            cluster.append(str(row['cluster']))
            row['id'] = {
                'id':str(row['cluster']),
                'name': "",
                'sumber' : row['sumber'],
                'link' : row['link'],
                'content' : row['content'][:300]
            }
            ans = {
                str(id)+'_|_'+str(row['cluster']) : row['id']
            }
            an = {
                'ae':ans
            }
            edges.append(an)
        unique_list = []
        for x in cluster:
            if x not in unique_list:
                id = x
                i = {
                    'id':id,
                    'name': "cluster "+id,
                    'content' : ''
                }
                ans = {
                    id : i
                }
                an = {
                    'an':ans
                }
                clusters.append(an)
        hasil = {
            'node' : clusters,
            'edge' : edges
        }
        # print(hasil)
        return hasil