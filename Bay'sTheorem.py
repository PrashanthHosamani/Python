#P(B): Marginal probability of B.

def bayes_theorem(prior_A, likelihood_B_given_A, marginal_B):
    
    #Implements bayes theorem.
    
    
    posterior_A_given_B = (likelihood_B_given_A) / marginal_B
    return posterior_A_given_B

#example: Medical test fot a disease
#P(Disease) = 0.01, P(Postitive|Disease) = 0.99, P(Positive)= 0.05

prior = 0.01
likelihood = 0.99
marginal = 0.05

posterior = bayes_theorem(prior, likelihood, marginal)
print(f"Prosterior Probability P(Disease|Positive): {posterior:.4f}")



#Part 2: Bayesian network


