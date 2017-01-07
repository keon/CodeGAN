# CodeGAN 

Source Code Generation with Generative Adversarial Networks (SeqGAN)

## Requirements: 
* Tensorflow r0.11
* Cuda 7.5 or higher (for GPU)  
* nltk python package

## Comparison with other Models & Experiments

### Code Written by: **Character Recurrent Neural Network**
```python
def media ( self  ) :
    choices = s
def cgets_to_reating_request ( _default  ) :
    charset = _errors
def field_with__ in get_language (  ) :
    if func . __iter__

import unicode_litible
self . encode ( self  ) :
    if isinstance ( value , items  ) :
    if not os . path . lower for dotage_nurn :
        pass
    except XTERTAD_MI_NUN_FITCL

@ DEFILL
self . _funacod_location . copy ( i  )
    return s
```

It writes some texts that look like a program.
But clearly Char-RNN is a bad programmer. (it can implement functions).

### Code Written by: **Word Recurrent Neural Network**
```python
class number_format ( _html_parser . signals . alias  ) :
    def __init__ ( self , commit = False  ) :
        widgets = value
        content = [  ]
        s = key
        self . kwargs = current_app
        self . _clean_form (  )

    def required ( self , name  ) :
        value = self . add_prefix ( name  )

    def nud ( self , filter_expr , subdir  ) :
        value = force_text ( value  )
        else :
            return self . _headers . contents tempdir . set_app ( cls  )
        if timezone . to_locale ( value  ) :
            return formats . zone msgs
```

As you can see, Word-RNN can hold on to the context longer than Char-RNN,
thus it writes a longer program. (it can implement classes).

### Code Written By: **CodeGAN - Reinforce**

Debugging...

### Code Written By: **CodeGAN - Polcy Gradient**

```python
' , 5 : _ ( : ] for key , default = '/dev/null ' , help = 'nominates a
, 'sender ' , 'reply-to ' , 'to ' , 400 , '-a ' , action = 'store ' ,
' , ord ( ext , true ) : 
 	 	 	 	 	 	 declared_fields . choice_cache =
' ) , 'max_decimal_places ' : ungettext_lazy ( 'ensure that there are no more than % ( max ) s
) : 
 	 def __init__ ( self , * args , ** kwargs ) : 
 	 	 	
' , action = 'store_false ' , dest = 'load_initial_data ' , default = true , help = 'tells django
, ( k , { ) ) , 'max_whole_digits ' : ungettext_lazy ( 'ensure that there are no more than
, 'migrate_failure ' : { 'fg ' : 'red ' , 'opts ' : ( 'bold ' , ) }
, exclude = use_natural_foreign_keys == '' and not self . port is none : 
 	 	 	 	 	
are no more than % ( max ) s is not . ' ' . ' ) 
 collect .
' , action = 'store_false ' , dest = 'load_initial_data ' , default = false , help = 'tells =
) : 
 	 	 def __init__ ( self , * args , ** kwargs ) : 
 	 	
, 'get_language_bidi ' , 'hiddeninput ' , 'multiplehiddeninput ' , 'clearablefileinput ' , 'fileinput ' , 'dateinput ' , 'datetimeinput
' ) 
 parser . add_argument ( ' -- database ' -- 'mar ' : ( ) -- 'bpython '
, { 'fg ' : 'red ' , 'opts ' : ( 'bold ' , ' ) , 'sender '
) 
 parser . add_argument ( ' -- no-initial-data ' , action = 'store_false ' , dest = 'load_initial_data '
) : 
 return mark_safe ( '\n ' . join ( model ) s . ' , } 
 	
= ' ) , 'max_decimal_places ' : ungettext_lazy ( 'ensure that there are no more than % ( max )
) , 'max_decimal_places ' : ungettext_lazy ( 'ensure that there are no more than % ( max ) s {
' , help = 'tells django not not pk . using argument class natural-foreign appcommand ( ) : 
 from
* args , s = ' , `` '' , 1 : 
 	 	 	 	 	 return ``
) : 
 	 	 def __init__ ( self , * args , ** kwargs ) : 
 	 	
' , action = 'store_false ' , dest = 'load_initial_data ' , default = true , help = 'tells django
' ) 
 parser . add_argument ( ' -- all ' , '-a ' , action = 'store_true ' ,
) } 
 	 def __init__ ( self , * args , ** kwargs ) : 
 	 	 	
, action = 'store_false ' , dest = 'load_initial_data ' , default = true , help = minute == default_db_alias
, 'sender ' , 'reply-to ' , 'to ' , 'cc ' , 'bcc ' , 'resent-from ' , keyerror
	 	 def __init__ ( self , * args , ** kwargs ) : 
 	 	 	 self .
, 'migrate_failure ' : { 'fg ' : 'red ' , 'opts ' : ( 'bold ' , ) }
, 'http_bad_request ' : { 'fg ' : 'red ' , 'opts ' : ( 'bold ' , ) }
' , 'httpresponseservererror ' , 'http404 ' , 'badheadererror ' , 'fix_location_header ' , 'jsonresponse ' , 'conditional_content_removal ' ,
' ) 
```

SeqGAN quickly loses the context in a long sequence.
I will keep improve this in the future.

## Model

The model used for the code generation is called Sequence Generative Adversarial Nets (with Policy Gradient).

![](https://github.com/keonkim/CodeGAN/blob/master/images/seqgan.png)

The illustration of SeqGAN.
Left: D is trained over the real data and the generated data by G.
Right: G is trained by policy gradient where the final reward signal is provided by D and
is passed back to the intermediate action value via Monte Carlo search.

The research paper [SeqGAN: Sequence Generative Adversarial Nets with Policy Gradient](http://arxiv.org/abs/1609.05473)
has been accepted at the Thirty-First AAAI Conference on Artificial Intelligence (AAAI-17).
The final version of the paper will be updated soon.

## Run
Move to codegan-pg folder and run
```
python pretrain_experiment.py
```
will start maximum likelihood training with default parameters.
In the same folder, run
```
python sequence_gan.py
```
will start SeqGAN training.


## Aknowledgements
This is one of many exiting projects going on in the *DeepCoding Project*.
Stay tuned for more awesome stuff.

Note:
I built it on top of the original implementation of [SeqGAN](https://github.com/LantaoYu/SeqGAN) which is 
based on the [previous work by ofirnachum](https://github.com/ofirnachum/sequence_gan).
Many thanks to [ofirnachum](https://github.com/ofirnachum) and [LantaoYu](https://github.com/LantaoYu).

After running the experiments, the learning curve should be like this:  
![](https://github.com/keonkim/CodeGAN/blob/master/images/lc.png)
