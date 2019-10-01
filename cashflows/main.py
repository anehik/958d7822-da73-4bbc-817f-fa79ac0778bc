import fire
import json
from util import InvestmentProject

class Main(object):

    @staticmethod
    def describe_investment(filepath, hurdle_rate=None):
        investment_project = InvestmentProject.from_csv(filepath=filepath, hurdle_rate=hurdle_rate)
        description = investment_project.describe()
        print(json.dumps(description, indent=4))

        print('What does it means when the internal-rate of return is greater than the hurdle rate?    ')
        print('When the internal-rate of return is greater than the hurdle rate, it means that the investment is profitable ')

        print('Can the net present value be negative? Why?  ')
        print('The net present value cant be negative, because is a sum of positive values so these values are positive')


    @staticmethod
    def plot_investment(filepath, save="", show=False):
        # TODO: implement plot_investment method
        #raise NotImplementedError
        print('Karely Mayorquin')
        investment = InvestmentProject.from_csv(filepath=filepath)
        fig = investment.plot(show=show)
        if save:
            fig.savefig("pic.png")
        return



if __name__ == "__main__":
    fire.Fire(Main)