def write_ply_with_colors(vertex, tri, wfp):
	header = """ply\nformat ascii 1.0\nelement vertex {}\nproperty float x\nproperty float y\nproperty float z\nproperty uchar red\nproperty uchar green\nproperty uchar blue\nelement face {}\nproperty list uchar int vertex_indices\nend_header"""

	n_vertex = vertex.shape[0]
	n_face = tri.shape[1]
	header = header.format(n_vertex, n_face)

	with open(wfp, 'w') as f:
		f.write(header + '\n')
		for i in range(n_vertex):
			x,y,z,r,g,b = vertex[i, :]
			f.write('{:.4f} {:.4f} {:.4f} {:d} {:d} {:d}\n'.format(x, y, z, int(r), int(g), int(b)))
		for i in range(n_face):
			idx1, idx2, idx3 = tri[:, i]
			f.write('3 {} {} {}\n'.format(idx2 - 1, idx1 - 1, idx3 - 1))
	print('Dump to {}'.format(wfp))


def write_obj_with_colors(vertex, tri, wfp):
	n_vertex = vertex.shape[0]
	n_face = tri.shape[1]

	with open(wfp, 'w') as f:
		for i in range(n_vertex):
			x,y,z,r,g,b = vertex[i, :]
			f.write('v {:.4f} {:.4f} {:.4f} {:d} {:d} {:d}\n'.format(x, y, z, int(r), int(g), int(b)))
		for i in range(n_face):
			idx1, idx2, idx3 = tri[:, i]
			f.write('f {} {} {}\n'.format(idx2, idx1, idx3))
	print('Dump to {}'.format(wfp))

def str2bool(v):
	if v.lower() in ('yes', 'true', 't', 'y', '1'):
		return True
	elif v.lower() in ('no', 'false', 'f', 'n', '0'):
		return False
	else:
		raise argparse.ArgumentTypeError('Boolean value expected')


def main():
	pass


if __name__ == '__main__':
	main()