# CS50 AI Heredity

Heredity uses Bayesian networks to calculate the probability of genetic traits being passed down through generations. The program models inheritance of traits like the presence of a particular gene to predict outcomes for family members.

## Contributions

`heredity.py`:

`joint_probability`: Calculates the joint probability of a set of people having specific gene copies and traits. It takes into account genetic inheritance and mutation probabilities. For individuals without parent information, it uses predefined probabilities; for those with known parents, it factors in the likelihood of each parent passing on a gene.

`update`: Updates the existing probability distributions for each person in the dataset based on a given joint probability. It adds the calculated probability to the appropriate gene and trait categories without returning a value.

`normalize`: Adjusts the probability distributions for each person so that the total sum for each distribution equals 1, while maintaining the relative proportions of the values. It modifies the probabilities dictionary in place.

### Testing

A test script (`test_heredity.py`) has been developed to verify the correct operation of all listed functions.

### Technologies Used

- `Unittest`

### Usage

- main: `python3 heredity.py data.csv`
- test: `python3 test_heredity.py`