list=("raw_data_objaverse-xl_hf-objaverse-v1_glbs_000-007_140d61f5dab7490f8e071ec84b8a9d19.glb"\
      "raw_data_objaverse-xl_hf-objaverse-v1_glbs_000-007_bd19e56f0a3542339754b4a687cb1f92.glb"\
      "raw_data_objaverse-xl_hf-objaverse-v1_glbs_000-123_888cc4ce6b9b43cfb1e10de8546b57d1.glb"\
      "raw_data_objaverse-xl_hf-objaverse-v1_glbs_000-158_3c46de927cf7455fad598f238da5a4d8.glb"\
      "67f716516df3439db32325903e52bdde.glb")

for i in ${list[@]}; do 
    python demo.py -i ./examples/$i -o $i.obj
done