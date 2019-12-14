from scipy.io import loadmat
import numpy as np
import itertools 
from math import sqrt

class Mesh:
	def __init__(self, obj_file):
		self.obj_file = open(obj_file,'r')
		self.vertices = np.zeros((53215,6))
		self.tri = loadmat('./configs/tri.mat')['tri']

	def get_vertices_with_rgb(self,meshFile):
		vertices_with_rgb_complete_list = []
		vertices_with_rgb_list = []
		for i, line in enumerate(meshFile):
			if(line[0] == 'v'):
				vertices_with_rgb = line.strip('\n').split(" ")
				vertices_with_rgb_list.append(float(vertices_with_rgb[1]))
				vertices_with_rgb_list.append(float(vertices_with_rgb[2]))
				vertices_with_rgb_list.append(float(vertices_with_rgb[3]))
				vertices_with_rgb_list.append(float(vertices_with_rgb[4]))
				vertices_with_rgb_list.append(float(vertices_with_rgb[5]))
				vertices_with_rgb_list.append(float(vertices_with_rgb[6]))
				vertices_with_rgb_complete_list.append(vertices_with_rgb_list)
				vertices_with_rgb_list = []
			else:
				continue
		self.vertices = np.array(vertices_with_rgb_complete_list)


	def get_bfm_vertices(self, meshFile):
		vertices_with_rgb_complete_list = []
		vertices_with_rgb_list = []
		counter = 1
		for i, line in enumerate(meshFile):
			if(line[0] == 'v'):
				vertices_with_rgb = line.strip('\n').split(" ")
				vertices_with_rgb_list.append(float(vertices_with_rgb[1]))
				vertices_with_rgb_list.append(float(vertices_with_rgb[2]))
				vertices_with_rgb_list.append(float(vertices_with_rgb[3]))
				vertices_with_rgb_list.append(int(0))
				vertices_with_rgb_list.append(int(0))
				vertices_with_rgb_list.append(int(0))
				vertices_with_rgb_complete_list.append(vertices_with_rgb_list)
				vertices_with_rgb_list = []
			else:
				continue
		self.vertices = np.array(vertices_with_rgb_complete_list)

	def get_predicted_texture(self):
		morphable_model = loadmat('./configs/01_MorphableModel.mat')
		tex_PC = morphable_model['texPC'];
		tex_MU = morphable_model['texMU'];

		vertices = self.vertices[:,0:3]
		tex_Cp = (self.vertices[:,3:6]*255).astype(int)
		distances = []
		range1 = 1-0;
		vertices_len = len(vertices)

		for i in range(0, vertices_len):
			vertice1 = vertices[i,:]
			vertice2 = vertices[8317,:]
			distances.append(sqrt(pow(vertice2[0]-vertice1[0],2) + pow(vertice2[1]-vertice1[1],2) + pow(vertice2[2]-vertice1[2],2)))

		minimum = min(distances)
		maximum = max(distances)

		for i in range(0, vertices_len):
			distances[i]=abs(((distances[i]-minimum)/(maximum-minimum)) - 1);
			distances[i]=(distances[i] * range1) 
		weight1 = []
		for i in range(0,len(distances)):
			weight1.append(distances[i])
			weight1.append(distances[i])
			weight1.append(distances[i])
		
		weight2 = np.array([weight1]*np.shape(tex_PC)[1])
		weight1 = np.array(weight1)
		weight2 = np.transpose(weight2)
		
		tex_Cp = np.array(list(itertools.chain(*tex_Cp)))

		tex_MU = np.reshape(tex_MU,np.shape(tex_MU)[0])
		tex_lhs = np.transpose(np.multiply(tex_PC, weight2))
		tex_rhs = np.multiply((tex_Cp - tex_MU), weight1)
		tex_z = np.matmul(tex_lhs,tex_rhs)
		
		tex_Cb = np.matmul(tex_PC,tex_z)+tex_MU
		
		tex_C = np.multiply(tex_Cp,weight1) + np.multiply(tex_Cb, (1-weight1))
		tex_C = np.around(tex_C)
		tex_C = np.transpose(tex_C)
		tex_C = np.reshape(tex_C, (vertices_len,3))
		predicted_texture = tex_C  

		return predicted_texture 

	def map_to_ddfa(self, ddfa_mesh, texture_map_bfm):
		mapping = loadmat('./configs/BFM_exp_idx.mat')
		bfm_to_exp = mapping['trimIndex'].tolist() 
		bfm_to_exp = list(itertools.chain.from_iterable(bfm_to_exp))
		i = 0
		while i < len(bfm_to_exp):
			ddfa_mesh[i][3] = float(texture_map_bfm[bfm_to_exp[i]-1][0])
			ddfa_mesh[i][4] = float(texture_map_bfm[bfm_to_exp[i]-1][1])
			ddfa_mesh[i][5] = float(texture_map_bfm[bfm_to_exp[i]-1][2])
			i+=1
		
		self.vertices = np.array(ddfa_mesh)

	
	def map_to_bfm(self, bfm_mesh, mesh_to_map):
		mapping = loadmat('./configs/BFM_exp_idx.mat')
		bfm_to_exp = mapping['trimIndex'].tolist() 
		bfm_to_exp = list(itertools.chain.from_iterable(bfm_to_exp))
		i = 0
		while i < len(bfm_to_exp):
			bfm_mesh[bfm_to_exp[i]-1][3] = float(mesh_to_map[i][3])/255.0
			bfm_mesh[bfm_to_exp[i]-1][4] = float(mesh_to_map[i][4])/255.0
			bfm_mesh[bfm_to_exp[i]-1][5] = float(mesh_to_map[i][5])/255.0
			i+=1

		self.vertices = np.array(bfm_mesh)