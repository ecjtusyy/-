import argparse

import numpy as np

import genesis as gs



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vis", action="store_true", default=False)
    args = parser.parse_args()

    ########################## init ##########################
    gs.init(seed=0, precision="32", logging_level="debug")

    ########################## create a scene ##########################

    scene = gs.Scene(
        sim_options=gs.options.SimOptions(
            dt=0.0000000000000000000000000000000000001,
            substeps=10,
        ),
        mpm_options=gs.options.MPMOptions(
            lower_bound=(-0.95, -0.497, -3.5),
            upper_bound=(0.95, 0.497, 3.5),
            grid_density=64,
            enable_CPIC=True,
        ),
        fem_options=gs.options.FEMOptions(
            floor_height=1,

        ),
        viewer_options=gs.options.ViewerOptions(
            camera_pos=(1.2, 0.9, 3.5),
            camera_lookat=(0.0, 0.0, 0.0),
            camera_fov=35,
            max_FPS=120,
        ),
        show_viewer=True,
        vis_options=gs.options.VisOptions(
            visualize_mpm_boundary=True,

        ),
    )

    plane = scene.add_entity(
        material=gs.materials.Rigid(),
        morph=gs.morphs.URDF(file="urdf/plane/plane.urdf", fixed=True),
    )


    jikeng = scene.add_entity(
        material=gs.materials.FEM.Elastic(),
        morph=gs.morphs.Mesh(
            file="/home/robot/文档/Genesis-main/genesis/assets/meshes/my_obj/jikeng_try38.0.obj",
            scale=0.01,            
            euler=(0,0,0),
            pos=(0, 0, 0.254),
            fixed=True,
        ),
        surface=gs.surfaces.Rough(
            color=(0.6, 1.0, 0.8, 1.0),
        ),
    )

    tukeng = scene.add_entity(
        material=gs.materials.MPM.Sand(),
        morph=gs.morphs.Mesh(
            file="/home/robot/文档/Genesis-main/genesis/assets/meshes/my_obj/tukeng.obj",
            scale=0.01,            
            euler=(90,0,0),
            pos=(0, 0, 0.175),
            fixed=True,
        ),
        surface=gs.surfaces.Rough(
            color=(0.6, 1.0, 0.8, 1.0),
        ),
    )


    scene.build()

    horizon = 4000
    for i in range(horizon):
        scene.step()
        # print(scene.fem_solver.compute_vel(horizon))


if __name__ == "__main__":
    main()
