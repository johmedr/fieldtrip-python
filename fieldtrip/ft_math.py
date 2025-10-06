from fieldtrip._runtime import Runtime


def ft_math(*args, **kwargs):
    """
      FT_MATH performs mathematical operations on FieldTrip data structures,
        such as addition, subtraction, division, etc.

        Use as
          data = ft_math(cfg, data1, data2, ...)
        with one or multiple FieldTrip data structures as the input and the configuration
        structure cfg in which you specify the mathematical operation that is to be
        executed on the desired parameter from the data
          cfg.parameter = string, field from the input data on which the operation is
                          performed, e.g. 'pow' or 'avg'
          cfg.operation = string, for example '(x1-x2)/(x1+x2)' or 'x1/6'

        In the specification of the mathematical operation, x1 is the parameter obtained
        from the first input data structure, x2 from the second, etc.

        Rather than specifying the operation as a string that is evaluated, you can also
        specify it as a single operation. The advantage is that it is computed faster.
           cfg.operation = string, can be 'add', 'subtract', 'divide', 'multiply', 'log10', 'abs'
                            'sqrt', 'square'
        If you specify only a single input data structure and the operation is 'add',
        'subtract', 'divide' or 'multiply', the configuration should also contain:
          cfg.scalar    = scalar value to be used in the operation
          cfg.matrix    = matrix with identical size as the data, it will be element-wise be applied

        The operation 'add' is implemented as follows
          y = x1 + x2 + ....
        if you specify multiple input arguments, or as
          y = x1 + s
        if you specify one input argument and a scalar value.

        The operation 'subtract' is implemented as follows
          y = x1 - x2 - ....
        if you specify multiple input arguments, or as
          y = x1 - s
        if you specify one input argument and a scalar value.

        The operation 'divide' is implemented as follows
          y = x1 ./ x2
        if you specify two input arguments, or as
          y = x1 / s
        if you specify one input argument and a scalar value.

        The operation 'multiply' is implemented as follows
          y = x1 .* x2
        if you specify two input arguments, or as
          y = x1 * s
        if you specify one input argument and a scalar value.

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_DATATYPE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_math.m )

    Copyright (C) 2011-2021, Robert Oostenveld
    Copyright (C) 2022-, Jan-Mathijs Schoffelen and Robert Oostenveld

    This file is part of FieldTrip, see http://www.fieldtriptoolbox.org
    for the documentation and details.

    FieldTrip is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    FieldTrip is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with FieldTrip. If not, see <http://www.gnu.org/licenses/>.
    """

    return Runtime.call("ft_math", *args, **kwargs)
