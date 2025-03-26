from heredity import *
import unittest


class TestJointProbability(unittest.TestCase):
    def setUp(self):
        self.people = people = {
            'Harry': {
                'name': 'Harry',
                'mother': 'Lily',
                'father': 'James',
                'trait': None
            },
            'James': {
                'name': 'James',
                'mother': None,
                'father': None,
                'trait': True
            },
            'Lily': {
                'name': 'Lily',
                'mother': None,
                'father': None,
                'trait': False
            }
        }

        self.one_gene = {"Harry"}
        self.two_genes = {"James"}
        self.trait = {"James"}

    def test_joint_probability(self):
        expected_answer = 0.0026643247488
        self.assertAlmostEqual(joint_probability(self.people, self.one_gene, self.two_genes, self.trait), expected_answer)


class TestUpdate(unittest.TestCase):
    def setUp(self):
        self.probabilities = {
            "Harry": {
                "gene": {2: 0, 1: 0, 0: 0},
                "trait": {True: 0, False: 0}
            },
            "James": {
                "gene": {2: 0, 1: 0, 0: 0},
                "trait": {True: 0, False: 0}
            },
            "Lily": {
                "gene": {2: 0, 1: 0, 0: 0},
                "trait": {True: 0, False: 0}
            }
        }
    
    def test_update(self):
        one_gene = {"Harry"}
        two_genes = {"James"}
        have_trait = {"Harry", "James"}
        p = 0.02 

        expected_probabilities = {
            "Harry": {
                "gene": {2: 0, 1: 0.02, 0: 0},
                "trait": {True: 0.02, False: 0}
            },
            "James": {
                "gene": {2: 0.02, 1: 0, 0: 0},
                "trait": {True: 0.02, False: 0}
            },
            "Lily": {
                "gene": {2: 0, 1: 0, 0: 0.02},
                "trait": {True: 0, False: 0.02}
            }
        }

        update(self.probabilities, one_gene, two_genes, have_trait, p)
        self.assertEqual(self.probabilities, expected_probabilities)


class TestNormalize(unittest.TestCase):
    def setUp(self):
        self.probabilities = {
            "Harry": {
                "gene": {2: 0, 1: 0, 0: 0},
                "trait": {True: 0.1, False: 0.3}
            },
            "James": {
                "gene": {2: 0, 1: 0, 0: 0},
                "trait": {True: 0, False: 0}
            },
            "Lily": {
                "gene": {2: 0.3, 1: 0.5, 0: 0.7},
                "trait": {True: 0, False: 0}
            }
        }

    def test_normalise(self):
        
        expected_probabilities = {
            "Harry": {
                "gene": {2: 0, 1: 0, 0: 0},
                "trait": {True: 0.25, False: 0.75}
            },
            "James": {
                "gene": {2: 0, 1: 0, 0: 0},
                "trait": {True: 0, False: 0}
            },
            "Lily": {
                "gene": {2: 0.2, 1: 0.3333, 0: 0.4667},
                "trait": {True: 0, False: 0}
            }
        }

        normalize(self.probabilities)
        self.assertEqual(self.probabilities, expected_probabilities)

if __name__ == '__main__':
    unittest.main()