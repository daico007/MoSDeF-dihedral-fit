import pytest
import numpy as np
from mosdef_dihedral_fit.tests.base_test import BaseTest
from mosdef_dihedral_fit.utils.io import get_mosdef_dihedral_fit_fn
import mosdef_dihedral_fit.utils.math_operations as mdf_math


class TestMathOperations(BaseTest):
    # ********************************************
    # test the mdf_math.round_to_sig_figs (START)
    # ********************************************

    def test_round_to_3_default_sig_figs(self):
        test_sigfig_input_value = 12.283638245
        test_return_value = mdf_math.round_to_sig_figs(test_sigfig_input_value)

        assert test_return_value == 12.3

    def test_round_to_4_sig_figs(self):
        test_sigfig_input_value = 122.83638245
        test_return_value = mdf_math.round_to_sig_figs(
            test_sigfig_input_value, sig_figs=4)

        assert test_return_value == 122.8

    def test_round_to_6_sig_figs(self):
        test_sigfig_input_value = 0.12283638245
        test_return_value = mdf_math.round_to_sig_figs(
            test_sigfig_input_value, sig_figs=6)

        assert test_return_value == 0.122836

    def test_round_to_1_sig_figs(self):
        test_sigfig_input_value = 1228.3638245
        test_return_value = mdf_math.round_to_sig_figs(
            test_sigfig_input_value, sig_figs=1)

        assert test_return_value == 1000.0

    def test_round_to_2_sig_figs(self):
        test_sigfig_input_value = 122836.38245
        test_return_value = mdf_math.round_to_sig_figs(
            test_sigfig_input_value, sig_figs=2)

        assert test_return_value == 120000

    def test_round_to_0_sig_figs(self):
        test_sigfig_input_value = 12.283638245
        test_return_value = mdf_math.round_to_sig_figs(
            test_sigfig_input_value, sig_figs=0)

        assert test_return_value == 0.0

    # ********************************************
    # test the mdf_math.round_to_sig_figs (END)
    # ********************************************

    # ********************************************
    # test the normalize_vector_length (START)
    # ********************************************

    def test_normalize_vector_length_1(self):
        test_vector_input_value = [1.2, -2.3, 3.4]
        test_return_value = mdf_math.normalize_vector_length(
            test_vector_input_value)

        assert np.isclose(test_return_value, 4.27668095606862)

    def test_normalize_vector_length_2(self):
        test_vector_input_value = [4.2, 3.3, -2.4]
        test_return_value = mdf_math.normalize_vector_length(
            test_vector_input_value)

        assert np.isclose(test_return_value, 5.85576638878294)

    def test_normalize_vector_length_3(self):
        test_vector_input_value = [14.2, -23.3, -2.4]
        test_return_value = mdf_math.normalize_vector_length(
            test_vector_input_value)

        assert np.isclose(test_return_value, 27.391422014930146)

    # ********************************************
    # test the normalize_vector_length (END)
    # ********************************************

    # ********************************************
    # test the normalize_vector (START)
    # ********************************************

    def test_normalize_vector_1(self):
        test_vector_input_value = np.array([1.2, -2.3, 3.4])
        test_return_value = mdf_math.normalize_vector(test_vector_input_value)

        assert isinstance(test_return_value, np.ndarray)
        assert len(test_return_value) == 3
        assert np.isclose(test_return_value[0], 0.28059142)
        assert np.isclose(test_return_value[1], -0.53780023)
        assert np.isclose(test_return_value[2], 0.79500904)

    def test_normalize_vector_2(self):
        test_vector_input_value = np.array([4.2, 3.3, -2.4])
        test_return_value = mdf_math.normalize_vector(test_vector_input_value)

        assert isinstance(test_return_value, np.ndarray)
        assert len(test_return_value) == 3
        assert np.isclose(test_return_value[0], 0.71724173)
        assert np.isclose(test_return_value[1], 0.56354707)
        assert np.isclose(test_return_value[2], -0.40985242)

    def test_normalize_vector_3(self):
        test_vector_input_value = [14.2, -23.3, -2.4]
        test_return_value = mdf_math.normalize_vector(test_vector_input_value)

        assert isinstance(test_return_value, np.ndarray)
        assert len(test_return_value) == 3
        assert np.isclose(test_return_value[0], 0.51841047)
        assert np.isclose(test_return_value[1], -0.85063127)
        assert np.isclose(test_return_value[2], -0.08761867)

    def test_normalize_vector_3(self):
        with pytest.raises(
                ValueError,
                match=f"ERROR: The normal vector = 0, indicating that these lines or planes "
                      f"lay on top each other or are perpendicular. \n"
                      f"The input vector = \[0 0 0\]",
        ):
            test_vector_input_value = [0, 0, 0]
            test_return_value = mdf_math.normalize_vector(
                test_vector_input_value)

    # ********************************************
    # test the normalize_vector (END)
    # ********************************************

    # ********************************************
    # test the angle_between_2_vectors (START)
    # ********************************************

    def test_angle_between_2_vectors_1(self):
        test_vector_1_input_value = np.array([1.2, -2.3, 3.4])
        test_vector_2_input_value = np.array([2.1, -4.3, 6.4])
        test_return_value = mdf_math.angle_between_2_vectors(
            test_vector_1_input_value,
            test_vector_2_input_value
        )

        assert isinstance(test_return_value, float)
        assert np.isclose(test_return_value, 88.32356406902932)

    def test_angle_between_2_vectors_2(self):
        test_vector_1_input_value = np.array([1, 0, 0])
        test_vector_2_input_value = np.array([0, 1, 0])
        test_return_value = mdf_math.angle_between_2_vectors(
            test_vector_1_input_value,
            test_vector_2_input_value
        )

        assert isinstance(test_return_value, float)
        assert np.isclose(test_return_value, 90.0)

    def test_angle_between_2_vectors_3(self):
        test_vector_1_input_value = [1, 0, 0]
        test_vector_2_input_value = [0, 0, 1]
        test_return_value = mdf_math.angle_between_2_vectors(
            test_vector_1_input_value,
            test_vector_2_input_value
        )

        assert isinstance(test_return_value, float)
        assert np.isclose(test_return_value, 90.0)

    def test_angle_between_2_vectors_4(self):
        test_vector_1_input_value = [1, 0, 0]
        test_vector_2_input_value = [1, 1, 1]
        test_return_value = mdf_math.angle_between_2_vectors(
            test_vector_1_input_value,
            test_vector_2_input_value
        )

        assert isinstance(test_return_value, float)
        assert np.isclose(test_return_value, 70.52877936550931)

    def test_angle_between_2_vectors_5(self):
        test_vector_1_input_value = [0.999999999999999, 0, 0]
        test_vector_2_input_value = [-1, 0, 0]
        test_return_value = mdf_math.angle_between_2_vectors(
            test_vector_1_input_value,
            test_vector_2_input_value
        )

        assert isinstance(test_return_value, float)
        assert np.isclose(test_return_value, 180.0)

    def test_angle_between_2_vectors_6(self):
        test_vector_1_input_value = [0, 0.999999999999999, 0]
        test_vector_2_input_value = [0, 1, 0]
        test_return_value = mdf_math.angle_between_2_vectors(
            test_vector_1_input_value,
            test_vector_2_input_value
        )

        assert isinstance(test_return_value, float)
        assert np.isclose(test_return_value, 0.0)

    def test_angle_between_2_vectors_7(self):
        with pytest.raises(
                ValueError,
                match=f"ERROR: The 'vector_1' or 'vector_2', and  |vector_1||vector_2| == 0, which means the \n"
                      f"angle can not be calculated due to the divisor being zero in the formula; \n"
                      f"angle = arccos\[\(vector_1 dot vector_2\)/\(|vector_1||vector_2|\)\]",
        ):
            test_vector_1_input_value = [0, 0, 0]
            test_vector_2_input_value = [1, 1, 1]
            test_return_value = mdf_math.angle_between_2_vectors(
                test_vector_1_input_value,
                test_vector_2_input_value
            )

    def test_angle_between_2_vectors_8(self):
        with pytest.raises(
                ValueError,
                match=f"ERROR: The 'vector_1' or 'vector_2', and  |vector_1||vector_2| == 0, which means the \n"
                      f"angle can not be calculated due to the divisor being zero in the formula; \n"
                      f"angle = arccos\[\(vector_1 dot vector_2\)/\(|vector_1||vector_2|\)\]",
        ):
            test_vector_1_input_value = [1, 1, 1]
            test_vector_2_input_value = [0, 0, 0]
            test_return_value = mdf_math.angle_between_2_vectors(
                test_vector_1_input_value,
                test_vector_2_input_value
            )

    # ********************************************
    # test the angle_between_2_vectors (END)
    # ********************************************

    # ********************************************
    # test the dihedral_angle (START)
    # ********************************************
    def test_dihedral_angle_1(self):
        test_vectors_input_value = [
            [-1.157250, 0.086030, 1.008021],
            [-0.763996, -0.002151, 0.000087],
            [0.763996, -0.002151, -0.000087],
            [1.157250, 0.086030, -1.008021]
        ]
        test_return_value = mdf_math.dihedral_angle(
            test_vectors_input_value[0],
            test_vectors_input_value[1],
            test_vectors_input_value[2],
            test_vectors_input_value[3]
        )

        assert isinstance(test_return_value, float)
        assert np.isclose(test_return_value, -169.99976081114102)

    def test_dihedral_angle_2(self):
        test_vectors_input_value = [[0.087884, 1.169649, -1.004308], [0.000000, 0.770018, 0.000246], [0.000000, -0.770018, 0.000246], [-0.087884, -1.169649, -1.004308]

                                    ]
        test_return_value = mdf_math.dihedral_angle(
            test_vectors_input_value[0],
            test_vectors_input_value[1],
            test_vectors_input_value[2],
            test_vectors_input_value[3]
        )

        assert isinstance(test_return_value, float)
        assert np.isclose(test_return_value, -9.999650545677945)

    def test_dihedral_angle_3(self):
        test_vectors_input_value = [
            [-0.000003, 1.170693, -1.00809],
            [0.000000, 0.770615, 0.000082],
            [0.000000, -0.770615, 0.000082],
            [0.000003, -1.170693, -1.008099]
        ]
        test_return_value = mdf_math.dihedral_angle(
            test_vectors_input_value[0],
            test_vectors_input_value[1],
            test_vectors_input_value[2],
            test_vectors_input_value[3]
        )

        assert isinstance(test_return_value, float)
        assert np.isclose(test_return_value, 0.0)

    def test_dihedral_angle_4(self):
        test_vectors_input_value = [
            [-0.087902, 1.169402, -1.004392],
            [-0.000000, 0.770059, 0.000295],
            [0.000000, -0.770059, 0.000295],
            [0.087902, -1.169402, -1.004392]
        ]
        test_return_value = mdf_math.dihedral_angle(
            test_vectors_input_value[0],
            test_vectors_input_value[1],
            test_vectors_input_value[2],
            test_vectors_input_value[3]
        )

        assert isinstance(test_return_value, float)
        assert np.isclose(test_return_value, 10.000370937675179)

    def test_dihedral_angle_5(self):
        test_vectors_input_value = [
            [-0.995768, 1.159585, -0.172100],
            [0.000000, 0.765133, 0.003478],
            [-0.000000, -0.765133, 0.003478],
            [0.995768, -1.159585, -0.172100]
        ]
        test_return_value = mdf_math.dihedral_angle(
            test_vectors_input_value[0],
            test_vectors_input_value[1],
            test_vectors_input_value[2],
            test_vectors_input_value[3]
        )

        assert isinstance(test_return_value, float)
        assert np.isclose(test_return_value, 160.00030858947946)

    def test_dihedral_angle_6(self):
        test_vectors_input_value = [
            [-1.008027, 1.157050, -0.086196],
            [-0.000000, 0.764044, 0.001992],
            [-0.000000, -0.764044, 0.001992],
            [1.008027, -1.157050, -0.086196]
        ]
        test_return_value = mdf_math.dihedral_angle(
            test_vectors_input_value[0],
            test_vectors_input_value[1],
            test_vectors_input_value[2],
            test_vectors_input_value[3]
        )

        assert isinstance(test_return_value, float)
        assert np.isclose(test_return_value, 170.00033111684917)

    def test_dihedral_angle_7(self):
        test_vectors_input_value = [
            [-1.012181, 1.156071, -0.000004],
            [-0.000000, 0.763665, -0.000006],
            [-0.000000, -0.763665, -0.000006],
            [1.012181, -1.156071, -0.000004]
        ]
        test_return_value = mdf_math.dihedral_angle(
            test_vectors_input_value[0],
            test_vectors_input_value[1],
            test_vectors_input_value[2],
            test_vectors_input_value[3]
        )

        assert isinstance(test_return_value, float)
        assert np.isclose(test_return_value, -180.0)

    def test_dihedral_angle_error_1_equal_2(self):
        with pytest.raises(
                ValueError,
                match=f"ERROR: The one or more of the atom coordinates are the same when entered into \n"
                      f"the 'get_dihedral_angle' functions.  In order, the entered atom coordinates: \n"
                      f"atom_xyz_coord_1 = \[1, 2, 3\]; \n"
                      f"atom_xyz_coord_2 = \[1, 2, 3\]; \n"
                      f"atom_xyz_coord_3 = \[7, 8, 9\]; \n"
                      f"atom_xyz_coord_4 = \[10, 11, 12\]. "
        ):
            test_vectors_input_value = [
                [1, 2, 3],
                [1, 2, 3],
                [7, 8, 9],
                [10, 11, 12]
            ]
            test_return_value = mdf_math.dihedral_angle(
                test_vectors_input_value[0],
                test_vectors_input_value[1],
                test_vectors_input_value[2],
                test_vectors_input_value[3]
            )

    def test_dihedral_angle_error_1_equal_3(self):
        with pytest.raises(
                ValueError,
                match=f"ERROR: The one or more of the atom coordinates are the same when entered into \n"
                      f"the 'get_dihedral_angle' functions.  In order, the entered atom coordinates: \n"
                      f"atom_xyz_coord_1 = \[1, 2, 3\]; \n"
                      f"atom_xyz_coord_2 = \[4, 5, 6\]; \n"
                      f"atom_xyz_coord_3 = \[1, 2, 3\]; \n"
                      f"atom_xyz_coord_4 = \[10, 11, 12\]. "
        ):
            test_vectors_input_value = [
                [1, 2, 3],
                [4, 5, 6],
                [1, 2, 3],
                [10, 11, 12]
            ]
            test_return_value = mdf_math.dihedral_angle(
                test_vectors_input_value[0],
                test_vectors_input_value[1],
                test_vectors_input_value[2],
                test_vectors_input_value[3]
            )

    def test_dihedral_angle_error_1_equal_4(self):
        with pytest.raises(
                ValueError,
                match=f"ERROR: The one or more of the atom coordinates are the same when entered into \n"
                      f"the 'get_dihedral_angle' functions.  In order, the entered atom coordinates: \n"
                      f"atom_xyz_coord_1 = \[1, 2, 3\]; \n"
                      f"atom_xyz_coord_2 = \[4, 5, 6\]; \n"
                      f"atom_xyz_coord_3 = \[7, 8, 9\]; \n"
                      f"atom_xyz_coord_4 = \[1, 2, 3\]. "
        ):
            test_vectors_input_value = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [1, 2, 3]
            ]
            test_return_value = mdf_math.dihedral_angle(
                test_vectors_input_value[0],
                test_vectors_input_value[1],
                test_vectors_input_value[2],
                test_vectors_input_value[3]
            )

    def test_dihedral_angle_error_2_equal_3(self):
        with pytest.raises(
                ValueError,
                match=f"ERROR: The one or more of the atom coordinates are the same when entered into \n"
                      f"the 'get_dihedral_angle' functions.  In order, the entered atom coordinates: \n"
                      f"atom_xyz_coord_1 = \[1, 2, 3\]; \n"
                      f"atom_xyz_coord_2 = \[4, 5, 6\]; \n"
                      f"atom_xyz_coord_3 = \[4, 5, 6\]; \n"
                      f"atom_xyz_coord_4 = \[10, 11, 12\]. "
        ):
            test_vectors_input_value = [
                [1, 2, 3],
                [4, 5, 6],
                [4, 5, 6],
                [10, 11, 12]
            ]
            test_return_value = mdf_math.dihedral_angle(
                test_vectors_input_value[0],
                test_vectors_input_value[1],
                test_vectors_input_value[2],
                test_vectors_input_value[3]
            )

    def test_dihedral_angle_error_2_equal_4(self):
        with pytest.raises(
                ValueError,
                match=f"ERROR: The one or more of the atom coordinates are the same when entered into \n"
                      f"the 'get_dihedral_angle' functions.  In order, the entered atom coordinates: \n"
                      f"atom_xyz_coord_1 = \[1, 2, 3\]; \n"
                      f"atom_xyz_coord_2 = \[4, 5, 6\]; \n"
                      f"atom_xyz_coord_3 = \[7, 8, 9\]; \n"
                      f"atom_xyz_coord_4 = \[4, 5, 6\]. "
        ):
            test_vectors_input_value = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [4, 5, 6]
            ]
            test_return_value = mdf_math.dihedral_angle(
                test_vectors_input_value[0],
                test_vectors_input_value[1],
                test_vectors_input_value[2],
                test_vectors_input_value[3]
            )

    def test_dihedral_angle_error_3_equal_4(self):
        with pytest.raises(
                ValueError,
                match=f"ERROR: The one or more of the atom coordinates are the same when entered into \n"
                      f"the 'get_dihedral_angle' functions.  In order, the entered atom coordinates: \n"
                      f"atom_xyz_coord_1 = \[1, 2, 3\]; \n"
                      f"atom_xyz_coord_2 = \[4, 5, 6\]; \n"
                      f"atom_xyz_coord_3 = \[7, 8, 9\]; \n"
                      f"atom_xyz_coord_4 = \[7, 8, 9\]. "
        ):
            test_vectors_input_value = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [7, 8, 9]
            ]
            test_return_value = mdf_math.dihedral_angle(
                test_vectors_input_value[0],
                test_vectors_input_value[1],
                test_vectors_input_value[2],
                test_vectors_input_value[3]
            )
    # ********************************************
    # test the dihedral_angle (END)
    # ********************************************
