def __set_defaults_macnica_yocto():
    set_default('MACHINE', 'rv1108-minievb')
    set_default('DISTRO', 'oel')
    set_default('SDKMACHINE', 'x86_64')


def __after_init_macnica_yocto():
    PLATFORM_ROOT_DIR = os.environ['PLATFORM_ROOT_DIR']

    append_layers([ os.path.join(PLATFORM_ROOT_DIR, 'sources', p) for p in
                    [
                        'meta-openembedded/meta-oe',
                        'meta-macnica',
                    ]])

run_set_defaults(__set_defaults_macnica_yocto)
run_after_init(__after_init_macnica_yocto)
