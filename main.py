import argparse
from utils.inference import write_obj_with_colors, write_ply_with_colors, str2bool
from utils.texture import Mesh

def main(args):
	ddfa_mesh = Mesh(args.obj)
	ddfa_mesh.get_vertices_with_rgb(ddfa_mesh.obj_file)

	print("BFM Mapping for Texture Prediction Started...")
	bfm_mesh = Mesh(args.bfm)
	bfm_mesh.get_bfm_vertices(bfm_mesh.obj_file)
	ddfa_mesh.map_to_bfm(bfm_mesh.vertices, ddfa_mesh.vertices)
	print("BFM Mapping for Texture Prediction Completed")

	print("Predicting Ear and Neck Texture...")
	final_texture = ddfa_mesh.get_predicted_texture()
	print("Predicting Ear and Neck Texture Completed")

	ddfa_mesh = Mesh(args.obj)
	ddfa_mesh.get_vertices_with_rgb(ddfa_mesh.obj_file)
	ddfa_mesh.map_to_ddfa(ddfa_mesh.vertices, final_texture)

	if(args.dump_obj):
		write_obj_with_colors(ddfa_mesh.vertices, ddfa_mesh.tri, './samples/output.obj')

	if(args.dump_ply):
		write_ply_with_colors(ddfa_mesh.vertices, ddfa_mesh.tri, './samples/output.ply')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='BFM Texture Fitting Pipeline ')
    parser.add_argument('-o', '--obj', default='./sample_ddfa.obj',
                        help='path to .obj (ddfa) file')
    parser.add_argument('-d', '--bfm', default='./configs/bfm.obj',
                        help='path to sample bfm mesh used for mapping ddfa to bfm')
    parser.add_argument('--dump_ply', default='True', type=str2bool)
    parser.add_argument('--dump_obj', default='True', type=str2bool)

    args = parser.parse_args()
    main(args)


