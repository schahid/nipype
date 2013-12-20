# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.dti import ProbTrackX
def test_ProbTrackX_inputs():
    input_map = dict(rand_fib=dict(argstr='--randfib=%d',
    ),
    verbose=dict(argstr='--verbose=%d',
    ),
    out_dir=dict(argstr='--dir=%s',
    genfile=True,
    ),
    waypoints=dict(argstr='--waypoints=%s',
    ),
    mask2=dict(argstr='--mask2=%s',
    ),
    phsamples=dict(mandatory=True,
    ),
    seed=dict(mandatory=True,
    argstr='--seed=%s',
    ),
    n_steps=dict(argstr='--nsteps=%d',
    ),
    seed_ref=dict(argstr='--seedref=%s',
    ),
    dist_thresh=dict(argstr='--distthresh=%.3f',
    ),
    use_anisotropy=dict(argstr='--usef',
    ),
    network=dict(argstr='--network',
    ),
    sample_random_points=dict(argstr='--sampvox',
    ),
    os2t=dict(argstr='--os2t',
    ),
    avoid_mp=dict(argstr='--avoid=%s',
    ),
    target_masks=dict(argstr='--targetmasks=%s',
    ),
    step_length=dict(argstr='--steplength=%.3f',
    ),
    n_samples=dict(argstr='--nsamples=%d',
    usedefault=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    thsamples=dict(mandatory=True,
    ),
    s2tastext=dict(argstr='--s2tastext',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    xfm=dict(argstr='--xfm=%s',
    ),
    samples_base_name=dict(usedefault=True,
    argstr='--samples=%s',
    ),
    args=dict(argstr='%s',
    ),
    inv_xfm=dict(argstr='--invxfm=%s',
    ),
    force_dir=dict(usedefault=True,
    argstr='--forcedir',
    ),
    mesh=dict(argstr='--mesh=%s',
    ),
    stop_mask=dict(argstr='--stop=%s',
    ),
    fibst=dict(argstr='--fibst=%d',
    ),
    random_seed=dict(argstr='--rseed',
    ),
    opd=dict(usedefault=True,
    argstr='--opd',
    ),
    mod_euler=dict(argstr='--modeuler',
    ),
    mask=dict(mandatory=True,
    argstr='-m %s',
    ),
    loop_check=dict(argstr='--loopcheck',
    ),
    c_thresh=dict(argstr='--cthr=%.3f',
    ),
    fsamples=dict(mandatory=True,
    ),
    correct_path_distribution=dict(argstr='--pd',
    ),
    mode=dict(argstr='--mode=%s',
    genfile=True,
    ),
    output_type=dict(),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    )
    inputs = ProbTrackX.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_ProbTrackX_outputs():
    output_map = dict(targets=dict(),
    fdt_paths=dict(),
    particle_files=dict(),
    log=dict(),
    way_total=dict(),
    )
    outputs = ProbTrackX.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value