# CodeGAN 

Source Code Generation with Generative Adversarial Networks (SeqGAN)

## Requirements: 
* Tensorflow r0.11
* Cuda 7.5 or higher (for GPU)  
* nltk python package

## Comparison with other Models & Experiments

**Character Recurrent Neural Network**
```
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

It writes some text that looks like a program.
But clearly Char-RNN is a bad programmer.

**Word Recurrent Neural Network**
```
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
thus it writes a longer code that is stable.

**CodeGAN - Reinforce**

Debugging...

**CodeGAN - Polcy Gradient**

```
(().__doc__=func.mime.<month>\d{1,2})-(?
contents.rel.creation.utils.models.tzinfo.creation.template.management.image.utils.utils.utils..value,self.dirname(writer.month,d._meta.core.data.isdir(os.match(bmatch.value,self.introspection.write(self.six.=self._archive.name=nameself.quote_name(self.dicts.tzinfo.utils.core.attname]=.')parser.%new_path,self.__args,**self.pk.add(opts.model.get(',','._out.compress(pickle.children.checks.lru_cacheinstead._out.style.nodelist_true.xml.management.path.dayifself.empty_form.utils.!
template..errnoore.field_name).options._current[field.%s.mail.paginator.iteritems(self.serializers.day,dt.match(bmatch._default_manager.fk.utils.__class__.data.xml.rawdataself.write(self.append(self._dir)or(e.widgets=copy._pk_field.migrations.utils.initial.decimal_places).models.pk.servers..__unicode__().utils.utils.can_write.nodelist.')parser.style.backends.platform.style.fk.stdout.stderr.ops.utils._meta.match(outer.options.append(self.six.ops.field.contentifsix.style.utils.kwargs.six.fileorself.choices.utils.path.core.utils.queryset.core.fileno(),sys.utils.utils.to.management.utils.::(?
utils._meta.__dict__.validators.abspath(os.platform.')parser.'._tzname=self.!
utils.forms.path.date.match(register_to.value,self._func_pathself.path.*ritem.loader.utils.attname]=.endswith('.data.file)withio.datetime.json_kwargs.loader.deleted_objects.value==self.introspection.forms.loader.dup2(si.')parser.fk.remove(self.six._servers=server.join(app_config.iteritems(sub_match.xml.%self.dst(self.core.schemeandparsed.data.path.__class__._cache.|re.utils.append(self.management.path.connection.loader._meta.stdout.object.six.moves.write(self.utils.settings.path.template.db.object.urllib.moves._meta.')parser.core.second,dt.style._stream,self.using].level<checks.dumps({f:e.style.utils.path.graph.0.ignore=options.core.stdout.:(?
path.widget.style.stream._out=outself.xml.widget.path..content).compile(r(^[!
environ.')parser.stdout.datetime.core.andnote.utils.moves.moves.size=sizeself.http._errors[field].core.stdout.*?
__name__,bits.))\.://,re.rel.#$%&'*+/=?
db.:\.isdir(os.utils.write(self.utils.core.path.path.=y._css.:\.data.write(writer.migrations.files,self.*?)))]))})>'))))))')'))')))')))]'))'))))))</month>)
```

Obviously, something went wrong.
I will investigate this after the finals. :)

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
