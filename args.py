def test_var_args(f_arg, *args):
    print("first normal arg:", f_arg)
    for arg in args:
        print("another arg through *argv :", arg)

test_var_args('yasoob','python','eggs','test')

